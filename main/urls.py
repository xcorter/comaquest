from django.conf.urls import patterns, include, url
from main import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)