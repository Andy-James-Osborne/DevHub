from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']

class UpdateProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    location = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))


    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'location']