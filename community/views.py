from django.shortcuts import render
from community.models import Post
from community.models import File


# Create your views here.
def index(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'community/index.html', context)


def detail(request, num):
    data = Post.objects.filter(id=num)
    context = {'data': data}
    return render(request, 'community/detail.html', context)
