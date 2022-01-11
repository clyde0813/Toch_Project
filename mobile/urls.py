from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.index, name='mobile_index'),
                  path('oneroom/', views.oneroom_index, name='mobile_oneroom'),
                  path('onroom/list', views.oneroom_list, name='oneroom_list'),
                  path('oneroom/detail/<int:num>', views.oneroom_detail, name='mobile_oneroom_detail'),
                  path('oneroom/edit', views.oneroom_edit, name='oneroom_edit')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
