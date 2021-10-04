from django.urls import path

from . import views

app_name = 'oneroom'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:num>', views.detail, name='detail')
]
