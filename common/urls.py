from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('login_Find', views.login_find, name='login_find'),
    path('signup/', views.signup, name='signup'),
    path('chat/community/', views.community_chat, name='community_chat'),
    path('chat/usedtrade/<int:num>', views.usedtrade_chat, name='usedtrade_chat'),
    path('chat/usedtrade/create/<int:chatroom_id>/', views.usedtrade_chat_send, name='usedtrade_chat_send'),
    path('service/', views.service, name='service'),

]
