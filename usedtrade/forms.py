from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'price', 'content']
        labels = {
            'title': '제목',
            'price': '가격',
            'content': '내용',
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        labels = {
            'file': '파일'
        }
