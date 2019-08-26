from django import forms
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,

)
from .models import Post, Comment,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
        'phone',
        'bio',
        'coverphoto',
        'image',
        'birthdate',
        ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = user
        fields = ['username','email','password1','password2']


#blog post/comment code

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text','image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
