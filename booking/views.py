from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django import template

from hotels.models import Hotel
from hotels.forms import HotelFilterForm


from rentals.models import Rental, Car, Bike
from .forms import CarFilterForm, BikeFilterForm

# Create your views here.
def search_hotel(request):
    params = request.GET

    # BUILDING QUERIES
    q = Hotel.objects

    if params.get('c'):
        q = q.filter(category__in=params.getlist('c'))
    if params.get('rt'):
        q = q.filter(room__roomtype__roomtype__in=params.getlist('rt'))

    hotels = q.order_by('name').all()
    form = HotelFilterForm(params)


    data = {
        'hotels': hotels,
        'form' : form,
        'active_tab': 'hotels',
    }

    return render(request, 'booking/hotels/results.html', data)

def search_car(request):
    params = request.GET
    form = CarFilterForm(params)

    # BUILDING QUERIES
    q = Car.objects
    if params.get('t'):
        q = q.filter(category__in=params.getlist('t'))
    if params.get('cc'):
        cc  = [int(x) for x in params.get('cc').split('-')]
        if len(cc) == 2:
            q = q.filter(cc__gte=cc[0]).filter(cc__lte=cc[1])
        else:
            q = q.filter(cc__gte=cc[0])

    print(form.is_valid())
    
    cars = q.order_by('model').all()
    data = {
        'cars' : cars,
        'form' : form,
        'active_tab': 'cars',
    }

    return render(request, 'booking/cars/results.html', data)

def search_bike(request):
    params = request.GET
    form = BikeFilterForm(params)

    # BUILDING QUERIES
    q = Bike.objects
    if params.get('c'):
        q = q.filter(category__in=params.getlist('c'))
    if params.get('cc'):
        bcc  = [int(x) for x in params.get('cc').split('-')]
        if len(bcc) == 2:
            q = q.filter(cc__gte=bcc[0]).filter(cc__lte=bcc[1])
        else:
            q = q.filter(cc__gte=bcc[0])

    print(form.is_valid())
    
    bikes = q.order_by('model').all()
    data = {
        'bikes' : bikes,
        'form' : form,
        'active_tab': 'bikes',
    }

    return render(request, 'booking/bikes/results.html', data)

def search_package(request):
    pass
