from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'www', 'Toch.urls', name='www'),
                         host(r'm', 'mobile.urls', name='m'),
                         )
