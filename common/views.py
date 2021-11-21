from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .models import Chat, ChatRoom


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
    return render(request, 'common/signup.html')


def page_not_found(request):
    return render(request, '404.html')


def usedtrade_chat(request, num):
    if num is 0:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = Chat.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        context = {'data': query_set, 'chatroom': chat_room_set}
        return render(request, 'common/usedtrade_chat.html', context)
    else:
        chat_room_set = ChatRoom.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = Chat.objects.filter(Q(author=request.user) | Q(receiver=request.user))
        query_set = query_set.filter(chatroom=num)
        context = {'data': query_set, 'chatroom': chat_room_set}
        return render(request, 'common/usedtrade_chat.html', context)


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
