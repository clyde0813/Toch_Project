from django.urls import path

from . import views

app_name = 'oneroom'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.detail, name='detail'),

    path('json/',views.oneroom_json, name='json'),
]
