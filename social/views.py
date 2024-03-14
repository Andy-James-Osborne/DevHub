from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm, UpdateProfileForm, UpdateUserForm
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

# @login_required
# def user_profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_vaild():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect('profile')
#     else:
#         pass
#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form,
#     }

#     return render(request, 'social/profile.html', context)

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

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post = post  
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    comments = Comment.objects.filter(post=post).order_by('-created_on')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "social/post_detail.html", context)

@login_required(login_url="login")
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is authorized to edit this post (optional)
    if post.author != request.user:
        return redirect('home', pk=pk)  # Redirect to post detail if not authorized

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)  # Update existing post
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to updated post detail
    else:
        form = PostForm(instance=post)  # Pre-fill form with existing post data

    context = {
        "post": post,
        "form": form,
    }

    return render(request, "social/edit_post.html", context)

@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')  # Redirect to homepage or a success page after deletion
    else:
        context = {
            "post": post,
        }

    return render(request, "social/delete_post.html", context)
    

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