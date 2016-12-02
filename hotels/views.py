from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Hotel
from django import template
from .forms import HotelFilterForm


# Create your views here.
def index(request):

    params = request.GET

    # BUILDING QUERIES
    q = Hotel.objects
    if params.get('c'):

        q = q.filter(category__in=params.getlist('c'))

    hotels = q.order_by('name').all()
    form = HotelFilterForm(params)

    data = {
        'hotels': hotels,
        'form' : form,
    }

    return render(request, 'hotels/index.html', data)


def detail(request, slug):

    hotel = get_object_or_404(Hotel, slug=slug)

    data = {
        'hotel': hotel,
    }

    return render(request, 'hotels/hotel.html', data)