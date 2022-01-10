from django_hosts.resolvers import reverse
from django.shortcuts import render
from .views_oneroom import *


# Create your views here.
def index(request):
    return render(request, 'mobile_template/main/index.html')
