
from django.contrib import admin
from   django.conf.urls import url
from django.urls import path, include

from django.conf.urls.static import static
import debug_toolbar
from django.conf import settings

# from charts.views import  ChartData
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')), 
                     
                  path('accounts/', include('accounts.urls')),
                  path('__debug__/', include(debug_toolbar.urls)),


                  path('contact', include('contacts.urls')),
                  path('charts/', include('charts.urls')),

                   
                    # url(r'^api/chart/data/$', ChartData.as_view()),
                   path('jobs/', include('jobs.urls')),
                    path(r'^api-auth/', include('rest_framework.urls'))



                  # path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)