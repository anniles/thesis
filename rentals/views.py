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


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)

    image_list = car.images.all()
    data = {
        'car': car,
        'image_list': image_list,
    }

    return render(request, 'rentals/car.html', data)

# class CarDetailView(generic.DetailView):
#     model = Car
#     template_name = 'rentals/car.html'

#     def get_queryset(self):
#         slug = self.kwargs.get(self.slug_url_kwarg)

#         return Car.objects.select_related('rental').filter(slug=slug)

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


def bike_detail(request, slug):
    bike = get_object_or_404(Bike, slug=slug)

    image_list = bike.images.all()

    data = {
        'bike': bike,
        'image_list': image_list,
    }

    return render(request, 'rentals/bike.html', data)

# class BikeDetailView(generic.DetailView):
#     model = Bike
#     template_name = 'rentals/bike.html'
