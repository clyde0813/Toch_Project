from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone

from community.models import Post as communityPost
from ip_gather import get_client_ip
from oneroom.models import Post as oneroomPost
from usedtrade.models import Post as usedtradePost
from .forms import *


# Create your views here.
def index(request):
    usedtrade_data = usedtradePost.objects.all().order_by('-create_date')
    usedtrade_paginator = Paginator(usedtrade_data, 4)
    usedtrade_data = usedtrade_paginator.get_page(1)

    oneroom_data = oneroomPost.objects.filter(browse_status=True).order_by('id')
    oneroom_paginator = Paginator(oneroom_data, 4)
    oneroom_data = oneroom_paginator.get_page(1)

    oneroom_data2 = oneroomPost.objects.filter(browse_status=True).order_by('-id')
    oneroom_paginator2 = Paginator(oneroom_data2, 4)
    oneroom_data2 = oneroom_paginator2.get_page(1)

    community_data = communityPost.objects.all().order_by('id')
    community_paginator = Paginator(community_data, 8)
    community_data = community_paginator.get_page(1)

    community_data2 = communityPost.objects.all().order_by('-id')
    community_paginator2 = Paginator(community_data2, 4)
    community_data2 = community_paginator2.get_page(1)

    context = {'usedtrade': usedtrade_data, 'oneroom': oneroom_data, 'oneroom2': oneroom_data2,
               'community': community_data, 'community2': community_data2}
    return render(request, 'main/index.html', context)


@login_required(login_url='common:login')
def mypage(request):
    return render(request, 'common/mypage_info.html')


def login_find(request):
    return render(request, 'common/login_Find.html')


def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('common:index')
    else:
        pass
        # user_form = UserForm(instance=request.user)

    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request):
    return render(request, '404.html')


@login_required(login_url='common:login')
def usedtrade_chat(request, num):
    if num is 0:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.exclude(chat_list__used_post__isnull=True)
        context = {'chatroom': chat_room_set}
        return render(request, 'common/usedtrade_chat.html', context)
    else:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.exclude(chat_list__used_post__isnull=True)
        query_set = Chat.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = query_set.filter(chatroom=num)
        usedtrade_info = usedtradePost.objects.filter(id=query_set.first().used_post_id)
        context = {'data': query_set, 'chatroom': chat_room_set, 'info': usedtrade_info}
        return render(request, 'common/usedtrade_chat.html', context)


@login_required(login_url='common:login')
def usedtrade_chat_send(request, chatroom_id):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.filter(id=chatroom_id)

        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.author_ip = get_client_ip(request)
            chat.create_date = timezone.now()
            author = chat_room_set.last().author
            if author == request.user:
                chat.receiver = chat_room_set.last().receiver
            else:
                chat.receiver = author
            chat.used_post_id = chat_room_set.last().chat_list.last().used_post_id
            chat.chatroom_id = chatroom_id
            chat.save()
            return redirect('common:usedtrade_chat', chatroom_id)


@login_required(login_url='common:login')
def community_chat(request):
    return render(request, 'common/community_chat.html')


@login_required(login_url='common:login')
def community_chat(request, num):
    if num is 0:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.exclude(chat_list__community_post__isnull=True)
        context = {'chatroom': chat_room_set}
        return render(request, 'common/community_chat.html', context)
    else:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.exclude(chat_list__community_post__isnull=True)
        query_set = Chat.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = query_set.filter(chatroom=num)
        usedtrade_info = usedtradePost.objects.filter(id=query_set.first().community_post_id)
        context = {'data': query_set, 'chatroom': chat_room_set, 'info': usedtrade_info}
        return render(request, 'common/community_chat.html', context)


@login_required(login_url='common:login')
def community_chat_send(request, chatroom_id):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        chat_room_set = chat_room_set.filter(id=chatroom_id)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.author_ip = get_client_ip(request)
            chat.create_date = timezone.now()
            author = chat_room_set.last().author
            if author == request.user:
                chat.receiver = chat_room_set.last().receiver
            else:
                chat.receiver = author
            chat.community_post_id = chat_room_set.last().chat_list.last().community_post_id
            chat.chatroom_id = chatroom_id
            chat.save()
            return redirect('common:community_chat', chatroom_id)


@login_required(login_url='common:login')
def service(request):
    return render(request, 'common/mypage_question.html')


def job_opening(request):
    return render(request, 'etc/job_opening.html')

# def email(request):
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Toch.settings.local")
#     otp = str(random.randint(100000, 999999))
#     email = EmailMessage(
#         'Hello',  # 제목
#         otp,  # 내용
#         'toch.text.email@gmail.com',  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
#         to=['eric3285@naver.com'],  # 받는 이메일 리스트
#     )
#     email.send()
#     context = {'otp': otp}
#     print(context)
#     return render(request, 'common/email.html', context)
