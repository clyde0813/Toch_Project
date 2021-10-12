import os
import random

from django.core.mail import EmailMessage
from django.shortcuts import render


# Create your views here.

def mypage(request):
    return render(request, 'common/mypage.html')


def signup(request):
    return render(request, 'common/signup.html')


def page_not_found(request):
    return render(request, '404.html')


def email(request):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Toch.settings.local")
    otp = str(random.randint(100000, 999999))
    email = EmailMessage(
        'Hello',  # 제목
        otp,  # 내용
        'toch.text.email@gmail.com',  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
        to=['eric3285@naver.com'],  # 받는 이메일 리스트
    )
    email.send()
    context = {'otp': otp}
    print(context)
    return render(request, 'common/email.html', context)
