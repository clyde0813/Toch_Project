from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    data = oneroom_post.objects.order_by('create_date')
    context = {'data_list': data}
    return render(request, 'oneroom/index.html', context)


def detail(request, num):
    data = oneroom_post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'oneroom/detail.html', context)
