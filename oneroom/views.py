from django.shortcuts import render
from django.db.models import Case, Q, When
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
    tmp = ['7', '6', '5', '4', '3', '2', '0', '1', '9', '8']
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(tmp)])
    data = Post.objects.filter(pk__in=tmp).order_by(preserved)
    context = {'data': data}
    return render(request, 'oneroom/test.html', context)
