from django.shortcuts import render


# Create your views here.

def mypage(request):
    return render(request, 'common/mypage.html')


def signup(request):
    return render(request, 'common/signup.html')

