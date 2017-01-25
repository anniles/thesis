from django.conf.urls import url

from . import views

app_name = 'user_profile'
urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^avatar/$', views.avatar, name='avatar'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^bookings/(?P<id>[\w-]+)/$', views.bookingItems, name='bookingItems'),
]