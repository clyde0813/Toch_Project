from django.urls import path
from . import views

app_name = 'mobile'

urlpatterns = [
    path('', views.index, name='index'),
]
