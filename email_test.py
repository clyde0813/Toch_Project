import os

from django.core.mail import EmailMessage

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Toch.settings.local")
email = EmailMessage(
    'Hello',  # 제목
    'Body goes here',  # 내용
    'toch.text.email@gmail.com',  # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
    to=['eric3285@naver.com'],  # 받는 이메일 리스트
)
email.send()
