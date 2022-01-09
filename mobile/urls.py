from django.urls import path
from . import views

app_name = 'mobile'

urlpatterns = [
    path('', views.index, name='index'),
    path('oneroom/', views.oneroom_index, name='oneroom_index'),
    path('onroom/list', views.oneroom_list, name='oneroom_list'),
    path('oneroom/detail', views.oneroom_detail, name='oneroom_detail'),
]
