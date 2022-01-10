from django.shortcuts import render, redirect

from .models import *


# Create your views here.

def index(request):
    data = Post.objects.order_by('create_date')
    image = File.objects.filter(rep=True)
    context = {'data': data, 'image': image}
    return render(request, 'oneroom/index.html', context)


def detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'oneroom/detail.html', context)
