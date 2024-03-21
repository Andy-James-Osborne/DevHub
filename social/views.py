from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, ProfileForm
from django.contrib import messages
from .models import Profile, Post, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    posts = Post.objects.all().order_by("created_on")
    context = {
        "posts": posts,
    }
    return render(request, 'social/home.html', context)


@login_required(login_url="login")
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    # Excludes the user that is logged in
    return render(request, 'social/profile_list.html', {"profiles": profiles})


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # Don't save yet, associate with user
            profile.user = request.user
            # Associate profile with current user
            profile.save()
            # Save the user profile
            messages.success(request, 'Profile Created!')
            return redirect('profile')
            # Redirect to profile page after creation
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, "social/profile_create.html", context)


@login_required(login_url="login")
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
        # Keeps the user information already filled out previously
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, "social/profile.html", context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save just yet
            post.author = request.user  # Assign current user as author
            post.save() # Save post
            messages.success(request, "Post was created successfully.")
            return redirect('home')  # Redirect to your desired page
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'social/create_post.html', context)


@login_required(login_url="login")
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()  # Form for comments
    liked = False # Likes are default to none

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # Don't save yet
            comment.post = post
            comment.author = request.user
            # Assign the user
            comment.save()
            # Save comment
            messages.success(request, "Comment was successful.")
            return redirect('post_detail', pk=post.pk)

    if request.method == "POST":
        if 'like' in request.POST:
            if request.user.is_authenticated:
                if post.likes.filter(id=request.user.id).exists():
                    post.likes.remove(request.user)
                    # If post is already liked it will be removed
                else:
                    post.likes.add(request.user)
                    # If post isn't liked will be added one like
        return redirect('post_detail', pk=post.pk)

    comments = Comment.objects.filter(post=post).order_by('-created_on')
    liked = request.user.is_authenticated and post.likes.filter(id=request.user.id).exists()
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "liked": liked,
    }

    return render(request, "social/post_detail.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is authorized to edit this post
    if post.author != request.user:
        return redirect('home', pk=pk)  # Redirect to post detail if not authorized

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # Update existing post
        if form.is_valid():
            form.save()
            messages.success(request, "Post was edited successfully.")
            return redirect('post_detail', pk=post.pk)  # Redirect to updated post detail
    else:
        form = PostForm(instance=post)  # Pre-fill form with existing post data

    context = {
        "post": post,
        "form": form,
    }

    return render(request, "social/edit_post.html", context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete() # Delete post
        messages.success(request, "Post was deleted successfully.")
        return redirect('home')  # Redirect to homepage or a success page after deletion
    else:
        context = {
            "post": post,
        }

    return render(request, "social/delete_post.html", context)


def edit_comment(request, pk):
    comments = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comments)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment was edited successfully.")
            return redirect('post_detail', pk=comments.post.pk)  # Redirect to updated post detail
    else:
        form = CommentForm(instance=comments)  # Pre-fill form with existing post data

    context = {
        "comments": comments,
        "form": form,
    }

    return render(request, "social/edit_comment.html", context)


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if request.method == "POST":
        comment.delete() # Delete comment
        messages.success(request, "Comment was deleted successfully.")
        return redirect('post_detail', pk=post.pk)

    context = {
        "comment": comment,
        "post": post

        }

    return render(request, "social/delete_comment.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Save user
            messages.success(request, "Sign up was successful.")
            return redirect('login') # return to login
    else:
        form = UserCreationForm() # Otherwise back to sign up form
    context = {'form': form}
    return render(request, 'social/signup.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # As long as username and password match data stored
        if user is not None:
            login(request, user)
            messages.success(request, "Login was successful.")
            return redirect('home')
        else:
            messages.info(request, "Please enter a valid login!")
            return redirect('login')

    else:
        form = AuthenticationForm()
        # Otherwise return to the login form
    context = {'form': form}
    return render(request, 'social/login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logout was successful.")
        return redirect('login')
        # When logged out return to login page
    else:
        return render(request, 'social/logout.html')
