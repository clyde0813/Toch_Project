
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['content']
