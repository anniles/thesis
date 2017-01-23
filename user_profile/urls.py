from django.conf.urls import url

from . import views

app_name = 'user_profile'
urlpatterns = [
    url(r'^avatar/$', views.avatar, name='avatar'),
    url(r'^$', views.profile, name='profile'),
]