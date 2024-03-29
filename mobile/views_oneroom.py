from django.db.models import Count
from django.utils import timezone
from django.shortcuts import render, redirect
from oneroom.models import *
from ip_gather import get_client_ip


def oneroom_index(request):
    contact = Contact.objects.all()
    data = Post.objects.all().annotate(num_like=Count('like_set')).order_by('-num_like')
    context = {'data': data, 'contact': contact}
    return render(request, 'mobile_template/oneroom/oneroom.html', context)


def oneroom_list(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_list.html', context)


def oneroom_detail(request, num):
    data = Post.objects.filter(id=num)
    like = PostLike.objects.filter(post_id=num)
    context = {'data': data, 'like': like}
    return render(request, 'mobile_template/oneroom/oneroom_detail.html', context)


def oneroom_like(request, num):
    try:
        like = PostLike.objects.get(post_id=num, ipAddress=get_client_ip(request), liked_date=timezone.now())
        like.delete()
    except:
        PostLike.objects.create(post_id=num, ipAddress=get_client_ip(request), liked_date=timezone.now())
    return redirect('mobile_oneroom_detail', num)


def oneroom_forSale(request):
    return render(request, 'mobile_template/oneroom/oneroom_forSale.html')


def oneroom_edit(request):
    data = PostStatus.objects.all()
    context = {'data': data}
    return render(request, 'mobile_template/oneroom/oneroom_edit.html', context)
