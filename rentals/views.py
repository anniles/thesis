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

    return render(request, 'rentals/cars.html', data)

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

    return render(request, 'rentals/bikes.html', data)


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = 'rentals/bike.html'