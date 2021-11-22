from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('job', views.job_opening, name='job_opening'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('login_Find', views.login_find, name='login_find'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('chat/community/<int:num>', views.community_chat, name='community_chat'),
    path('chat/community/create/<int:chatroom_id>/', views.community_chat_send, name='community_chat_send'),
    path('chat/usedtrade/<int:num>', views.usedtrade_chat, name='usedtrade_chat'),
    path('chat/usedtrade/create/<int:chatroom_id>/', views.usedtrade_chat_send, name='usedtrade_chat_send'),
    path('service/', views.service, name='service'),

]
