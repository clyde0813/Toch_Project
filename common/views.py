from django.shortcuts import render


# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


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


def usedtrade_chat(request):
    return render(request, 'common/usedtrade_chat.html')


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
