from django.urls import path, re_path
from django.conf.urls import url
from charts.views import *
 
urlpatterns = [
   url('', demo_piechart, name='demo_piechart'),
 
]
