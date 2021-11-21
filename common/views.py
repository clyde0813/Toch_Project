from importlib.resources import _

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
<<<<<<< HEAD

from .forms import UserForm
=======
from django.utils import timezone

from ip_gather import get_client_ip
>>>>>>> c2b354dbdd0a2d7906aad53471b8f073f21048a3
from usedtrade.models import Post as usedtradePost
from .forms import *


# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='common:login')
def mypage(request):
    return render(request, 'common/mypage_info.html')


def login(request):
    return render(request, 'common/login.html')


def login_find(request):
    return render(request, 'common/login_Find.html')


def signup(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('common:index')
    else:
        user_form = UserForm(instance=request.user)

    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request):
    return render(request, '404.html')


@login_required(login_url='common:login')
def usedtrade_chat(request, num):
    if num is 0:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        context = {'chatroom': chat_room_set}
        return render(request, 'common/usedtrade_chat.html', context)
    else:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = Chat.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = query_set.filter(chatroom=num)
        usedtrade_info = usedtradePost.objects.filter(id=query_set.first().used_post_id)
        context = {'data': query_set, 'chatroom': chat_room_set, 'info': usedtrade_info}
        return render(request, 'common/usedtrade_chat.html', context)


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


def community_chat(request):
    return render(request, 'common/community_chat.html')


def service(request):
    return render(request, 'common/mypage_question.html')

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
