from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Rental, Car, Bike
from django import template
from .forms import CarFilterForm, BikeFilterForm


# Create your views here.
def index_cars(request):
    params = request.GET

    # BUILDING QUERIES
    cars = Car.objects.order_by('model').all()
    data = {
        'cars' : cars,
        'active_tab': 'cars',
    }

    return render(request, 'rentals/cars_list.html', data)

# class CarIndexView(generic.ListView):
#     template_name = 'rentals/cars.html'
#     context_object_name = 'cars'

#     def get_queryset(self):
#         return Car.objects.order_by('model').all()


class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'rentals/car.html'

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)

        return Car.objects.select_related('rental').filter(slug=slug)

# BIKES
def index_bikes(request):
    params = request.GET
    form = BikeFilterForm(params)

    # BUILDING QUERIES
    bikes = Bike.objects.order_by('model').all()
    
    data = {
        'bikes' : bikes,
        'active_tab': 'bikes',
    }

    return render(request, 'rentals/bikes_list.html', data)


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = 'rentals/bike.html'