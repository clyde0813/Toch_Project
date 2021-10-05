from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'usedtrade/index.html')


def detail(request, num):
    return render(request, 'usedtrade/detail.html')


def create_post(request):
    return render(request, 'usedtrade/create_post.html')
