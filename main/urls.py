from django.conf.urls import patterns, include, url
from main import views
from comaquest import settings

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)