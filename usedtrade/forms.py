from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'content']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글'
        }


class NestedForm(forms.ModelForm):
    class Meta:
        model = Nested
        fields = ['content']
        labels = {
            'content': '대댓글'
        }
