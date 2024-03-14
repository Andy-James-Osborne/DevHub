from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
