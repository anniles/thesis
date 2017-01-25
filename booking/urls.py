from django.conf.urls import url

from . import views

app_name = 'booking'
urlpatterns = [
    url(r'^hotels/$', views.search_hotel, name='search_hotel'),
    url(r'^cars/$', views.search_car, name='search_car'),
    url(r'^bikes/$', views.search_bike, name='search_bike'),
    url(r'^packages/$', views.search_package, name='search_package'),
]