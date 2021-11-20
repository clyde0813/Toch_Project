from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('login_Find', views.login_find, name='login_find'),
    path('signup/', views.signup, name='signup'),
    path('chat/community/', views.community_chat, name='community_chat'),
    path('chat/usedtrade/', views.usedtrade_chat, name='usedtrade_chat'),
    path('service/', views.service, name='service'),

]
