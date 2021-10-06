from django.urls import path

from . import views

app_name = "usedtrade"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:num>', views.detail, name="detail"),
    path('create', views.create_post, name="create_post"),
    path('delete/<int:num>', views.delete_post, name="delete_post"),

]
