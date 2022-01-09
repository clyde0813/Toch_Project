from django.shortcuts import render
from oneroom.models import *


def oneroom_index(request):
    return render(request, 'mobile_template/oneroom/oneroom.html')


def oneroom_list(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_list.html', context)


def oneroom_detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data' : data}
    return render(request, 'mobile_template/oneroom/oneroom_detail.html', context)


def oneroom_forSale(request):
    return render(request, 'mobile_template/oneroom/oneroom_forSale.html')
