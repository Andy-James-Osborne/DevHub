from django.shortcuts import render, redirect
import cloudinary.uploader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Post, Follow, Like, Comment
from .forms import RegistrationForm, CommentForm
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
  posts = Post.objects.all().order_by('-creation_date')

  context = {'posts': posts}
  return render(request, 'hub/post_feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'hub/register.html', context)

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
    return render(request, 'hub/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

# @login_required
def profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST' and 'profile_picture' in request.FILES:
        uploaded_file = request.FILES['profile_picture']
        upload_result = cloudinary.uploader.upload(uploaded_file, public_id=user.username + '_profile_pic')
        user.profile_picture = upload_result['url']
        user.save()
    context = {'user': user}
    return render(request, 'hub/profile.html', context)


# @login_required
def post_feed(request):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.create(user=request.user, content=content)
        return redirect('post_detail', pk=post.pk)  
    else:
        return render(request, 'hub/post_form.html')


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    likes = Like.objects.filter(post=post).count() 
    comments = Comment.objects.filter(post=post).order_by('-creation_date')
    context = {'post': post, 'likes': likes, 'comments': comments}
    return render(request, 'post_detail.html', context)

# @login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if not Like.objects.filter(user=request.user, post=post).exists():
        Like.objects.create(user=request.user, post=post)
    return redirect('post_detail', pk=post.pk)


from django.shortcuts import render, redirect

# @login_required
def comment_view(request, pk):
  post = Post.objects.get(pk=pk)
  likes = Like.objects.filter(post=post).count()
  comments = Comment.objects.filter(post=post).order_by('-creation_date')

  if request.method == 'POST':
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      # Create comment object but don't save yet
      comment = comment_form.save(commit=False)
      comment.user = request.user  # Set the current logged-in user
      comment.post = post  # Set the post the comment belongs to
      comment.save()  # Now save the comment with user and post assigned
      return redirect('post_detail', pk=post.pk)  # Redirect back to post detail
  else:
    comment_form = CommentForm()  # Create a blank comment form

  context = {'post': post, 'likes': likes, 'comments': comments, 'comment_form': comment_form}
  return render(request, 'post_detail.html', context)




