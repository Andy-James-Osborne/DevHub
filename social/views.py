from django.shortcuts import render, redirect
from .models import Profile, Post, Comment
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().order_by("created_on")
    context = {
        "posts": posts,
    }
    return render(request, 'social/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save just yet
            post.author = request.user  # Assign current user as author
            post.save()
            return redirect('home')  # Redirect to your desired page
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'social/home.html', context)

@login_required(login_url="login")
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
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