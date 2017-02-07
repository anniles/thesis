from django.conf.urls import url

from . import views

app_name = 'booking'
urlpatterns = [
    url(r'^hotels/$', views.search_hotel, name='search_hotel'),
    url(r'^hotels/(?P<slug>[\w-]+)/$', views.search_hotel_detail, name='search_hotel_detail'),
    url(r'^cars/$', views.search_car, name='search_car'),
    url(r'^cars/(?P<slug>[\w-]+)/$', views.search_car_detail, name='search_car_detail'),
    url(r'^bikes/$', views.search_bike, name='search_bike'),
    url(r'^bikes/(?P<slug>[\w-]+)/$', views.search_bike_detail, name='search_bike_detail'),
    url(r'^packages/$', views.search_package, name='search_package'),
    url(r'^booking/$', views.book, name='book'),
    url(r'^booking/thanks/$', views.thanku, name='thanku'),
]