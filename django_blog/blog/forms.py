from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Post, Comment, Tag

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # add tags field

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        # Add validation for tags if needed
        return tags
