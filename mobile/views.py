from django_hosts.resolvers import reverse
from django.shortcuts import render
from .views_oneroom import *


# Create your views here.
def index(request):
    homepage_url = reverse('mobile_oneroom', host='m')
    context = {'mobile_oneroom_url': homepage_url}
    return render(request, 'mobile_template/main/index.html', context)
