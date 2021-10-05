from django import forms

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = usedtrade_post
        fields = ['title', 'price', 'content']
        labels = {
            'title': '제목',
            'price': '가격',
            'content': '내용',
        }
