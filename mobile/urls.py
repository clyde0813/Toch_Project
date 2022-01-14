from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from common import views as common_views

urlpatterns = [
                  path('', views.index, name='mobile_index'),
                  path('oneroom/', views.oneroom_index, name='mobile_oneroom'),
                  path('onroom/list', views.oneroom_list, name='oneroom_list'),
                  path('oneroom/detail/<int:num>', views.oneroom_detail, name='mobile_oneroom_detail'),
                  path('oneroom/like/<int:num>', views.oneroom_like, name='mobile_oneroom_like'),
                  path('oneroom/edit', views.oneroom_edit, name='oneroom_edit'),
                  path('naverc24dc596faabf6aecb92e7c07cdb3f43.html/', common_views.tmp)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
