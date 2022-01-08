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
    path('service/', views.service, name='service'),

    # path('', views.fixing, name='index'),
    # path('job', views.fixing, name='job_opening'),
    # path('mypage/', views.fixing, name='mypage'),
    # path('login/', views.fixing, name='login'),
    # path('login_Find', views.fixing, name='login_find'),
    # path('logout/', views.fixing, name='logout'),
    # path('signup/', views.fixing, name='signup'),
    # path('service/', views.fixing, name='service'),
]
