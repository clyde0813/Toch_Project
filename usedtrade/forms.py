from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = usedtrade_post
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
