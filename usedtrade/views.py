from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *


# Create your views here.
def index(request):
    return render(request, 'usedtrade/index.html')


def detail(request, num):
    return render(request, 'usedtrade/detail.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('usedtrade:detail', post.id)
    else:
        form = PostForm(request.POST)
    context = {'form': form}
    return render(request, 'usedtrade/create_post.html', context)
