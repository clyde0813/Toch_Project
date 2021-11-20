from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import *


# Create your views here.

def index(request):
    data = Post.objects.order_by('create_date')
    context = {'data_list': data}
    return render(request, 'oneroom/index.html', context)


def detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'oneroom/detail.html', context)


def json(request):

    Attribution_dataset = Attribution.objects.all()

    queryset_json = serializers.serialize('json',Attribution_dataset)

    context = {"Attribution_dataset":Attribution_dataset, 'queryset_json':queryset_json}

    return JsonResponse({'queryset_json':queryset_json})
    # return render(request, 'oneroom/json.html',context)

