from django.conf.urls import url

from . import views

app_name = 'rentals'
urlpatterns = [
    url(r'^cars/$', views.CarIndexView.as_view(), name='cars'),
    url(r'^cars/(?P<slug>[\w-]+)/$', views.CarDetailView.as_view(), name='car'),
    url(r'^bikes/$', views.BikeIndexView.as_view(), name='bikes'),
    url(r'^bikes/(?P<slug>[\w-]+)/$', views.BikeDetailView.as_view(), name='bike'),
]