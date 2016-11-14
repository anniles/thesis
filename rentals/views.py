from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Rental, Car, Bike
from django import template


# Create your views here.
class CarIndexView(generic.ListView):
    template_name = 'rentals/cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.order_by('model').all()


class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'rentals/car.html'

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)

        return Car.objects.select_related('rental').filter(slug=slug)

class BikeIndexView(generic.ListView):
    template_name = 'rentals/bikes.html'
    context_object_name = 'bikes'

    def get_queryset(self):
        return Bike.objects.order_by('model').all()


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = 'rentals/bike.html'