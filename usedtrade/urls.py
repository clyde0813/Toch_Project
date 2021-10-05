from django.urls import path

from . import views

app_name = "usedtrade"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:num>', views.detail, name="detail"),

]
