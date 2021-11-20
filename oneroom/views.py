from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
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


def oneroom_json(request):
    Attribution_dataset = Attribution.objects.all().only('id', 'post', 'A', 'B', 'C', 'D', 'E')
    json_posts = json.dumps(Attribution_dataset)
    print(json_posts)
    # queryset_json = serializers.serialize('json', Attribution_dataset)

    context = {'queryset_json': queryset_json}

    return JsonResponse(context)
    # return render(request, 'oneroom/json.html',context)
