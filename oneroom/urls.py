from django.urls import path

from . import views
from common import views as common_views

app_name = "oneroom"

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:num>', views.detail, name='detail'),
    # path('test/', views.test, name='test'),

    path('', common_views.fixing, name='index'),
    path('test/', common_views.fixing, name='test'),
]
