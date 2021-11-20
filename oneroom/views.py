from django.http import JsonResponse
from django.shortcuts import render

from .models import *
from .serializer import AttributionSerializer


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
    queryset = Attribution.objects.all()
    serializer = AttributionSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
