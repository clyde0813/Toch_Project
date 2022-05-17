from django.shortcuts import render, redirect
from django.utils import timezone

from ip_gather import get_client_ip
from .forms import *


# Create your views here.
def index(request):
    data = Post.objects.order_by('create_date')
    context = {"data": data}
    return render(request, 'usedtrade/index.html', context)


def detail(request, num):
    if Post.objects.filter(id=num):
        post = Post.objects.order_by('create_date')
        data = Post.objects.filter(id=num).first()
        context = {'data': data, 'post': post}
        return render(request, 'usedtrade/detail.html', context)
    else:
        return render(request, '404.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form_file = FileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            post.author_ip = get_client_ip(request)
            post.delete_status = False
            post.save()
            if form_file.is_valid() and request.FILES.get("file") is not None:
                for i in request.FILES.getlist("file"):
                    form_file = FileForm(request, request.FILES)
                    file = form_file.save(commit=False)
                    file.create_date = post.create_date
                    file.post = post
                    file.file = i
                    file.author = request.user
                    file.author_ip = get_client_ip(request)
                    file.save()
            return redirect('usedtrade:detail', post.id)
    else:
        form = PostForm(request.POST)
    context = {'form': form}
    return render(request, 'usedtrade/create_post.html', context)


def delete_post(request, num):
    post = Post.objects.filter(id=num).first()
    post.delete()
    return redirect('usedtrade:index')


def create_comment(request, num):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = num
            comment.author_ip = get_client_ip(request)
            comment.create_date = timezone.now()
            comment.save()
    return redirect('usedtrade:detail', num)


def create_nested(request, num, num2):
    if request.method == 'POST':
        form = NestedForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_id = num2
            comment.create_date = timezone.now()
            comment.save()
    return redirect('usedtrade:detail', num)
