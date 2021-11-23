import json

from django.db.models import Case, When
from django.shortcuts import render, redirect

from .models import *


# Create your views here.

def index(request):
    data = Post.objects.order_by('create_date')
    context = {'data': data}
    return render(request, 'oneroom/index.html', context)


def detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'oneroom/detail.html', context)


def test(request):
    if request.method == "POST":
        data = json.load(request)
        tmp = data.split(',')
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(tmp)])
    data = Post.objects.filter(pk__in=tmp).order_by(preserved)
    context = {'data': data}
    print(data)
    return render(request, 'oneroom/index.html', context)
