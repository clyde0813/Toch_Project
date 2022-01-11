from django_hosts.resolvers import reverse
from django.shortcuts import render, redirect
from oneroom.models import *


def oneroom_index(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom.html', context)


def oneroom_list(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_list.html', context)


def oneroom_detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_detail.html', context)


def oneroom_like(request, num):
    data = Post_Status.objects.get(post_id=num)
    if data.like is None:
        data.like = 1
    else:
        data.like += 1
    data.save()
    return redirect('mobile_oneroom_detail', num)


def oneroom_forSale(request):
    return render(request, 'mobile_template/oneroom/oneroom_forSale.html')


def oneroom_edit(request):
    data = Post_Status.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_edit.html', context)
