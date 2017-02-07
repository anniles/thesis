from django.conf.urls import url

from . import views

app_name = 'rentals'
urlpatterns = [
    url(r'^cars/$', views.index_cars, name='cars'),
    url(r'^cars/(?P<slug>[\w-]+)/$', views.car_detail, name='car'),
    url(r'^bikes/$', views.index_bikes, name='bikes'),
    url(r'^bikes/(?P<slug>[\w-]+)/$', views.bike_detail, name='bike'),
]