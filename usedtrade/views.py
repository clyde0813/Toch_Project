from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *


# Create your views here.
def index(request):
    data = usedtrade_post.objects.order_by('created_date')
    context = {"data": data}
    return render(request, 'usedtrade/index.html', context)


def detail(request, num):
    if usedtrade_post.objects.filter(id=num):
        data = usedtrade_post.objects.filter(id=num)
        context = {'data': data}
        return render(request, 'usedtrade/detail.html', context)
    else:
        return render(request, '404.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('usedtrade:detail', post.id)
    else:
        form = PostForm(request.POST)
    context = {'form': form}
    return render(request, 'usedtrade/create_post.html', context)
