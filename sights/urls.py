from django.conf.urls import url

from . import views

app_name = 'sights'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
]