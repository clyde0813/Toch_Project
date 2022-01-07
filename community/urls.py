from django.urls import path

from . import views
from common import views as common_views

app_name = 'community'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:num>', views.detail, name='detail'),

    path('', common_views.fixing, name='index'),
]
