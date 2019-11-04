from django.conf import settings
import logging 
from sendsms import api
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from django.shortcuts import render

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
@cache_page(CACHE_TTL)
def index(request):
    return render(request, 'home/index.html')


def about(request):
    
    log = logging.getLogger(__name__)
    log.debug("Im Here to help you", exc_info=True)
    return render(request, 'home/about.html')