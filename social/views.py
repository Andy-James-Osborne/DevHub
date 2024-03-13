from django.shortcuts import render, redirect
from .forms import CommentForm, PostForm
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

def user_profile(request):
    return render(request, 'social/profile.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save just yet
            post.author = request.user  # Assign current user as author
            post.save()
            return redirect('home')  # Redirect to your desired page
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'social/create_post.html', context)

@login_required(login_url="login")
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()  # Form for comments
    edit_form = None  # Initialize edit form
    delete_confirmed = False  # Track deletion confirmation


    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = post  
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    # Check if the request is for editing the post
        if 'edit_post' in request.POST:
            edit_form = PostForm(request.POST, instance=post)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('post_detail', pk=post.pk)

        # Check if the request is for deleting the post
        if 'delete_post' in request.POST:
            if request.user.is_authenticated and (post.author == request.user or request.user.has_perm('yourapp.change_post')):  # Optional permission check
                post.delete()
                return redirect('post_list')  # Redirect to your post list URL
            else:
                # Handle unauthorized deletion attempt (optional: message or redirect)
                pass



    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        "edit_form": edit_form,
        "delete_confirmed": delete_confirmed,
    }

    return render(request, "social/post_detail.html", context)

    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'social/signup.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    else: 
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'social/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')