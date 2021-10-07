from django.urls import path

from . import views

app_name = "usedtrade"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:num>', views.detail, name="detail"),
    path('create', views.create_post, name="create_post"),
    path('delete/<int:num>', views.delete_post, name="delete_post"),
    path('comment/<int:num>', views.create_comment, name='create_comment'),
    path('nested/<int:num>/<int:num2>', views.create_nested, name='create_nested'),
]
