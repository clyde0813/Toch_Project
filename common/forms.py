<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
=======
from django import forms

from .models import *


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['content']
>>>>>>> c2b354dbdd0a2d7906aad53471b8f073f21048a3
