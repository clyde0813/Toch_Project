from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('path.to',
                         host(r'www', settings.ROOT_URLCONF, name='www'),
                         host(r'm', 'mobile.urls', name='m'),
                         )
