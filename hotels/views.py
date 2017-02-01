from itertools import groupby

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django import template

from .models import Hotel, Room
from .forms import HotelFilterForm



# Create your views here.
def index(request):

    params = request.GET

    # BUILDING QUERIES
    hotels = Hotel.objects.order_by('name').all()

    data = {
        'hotels': hotels,
        'active_tab': 'hotels',
    }

    return render(request, 'hotels/hotel_list.html', data)


def detail(request, slug):

    hotel = get_object_or_404(Hotel, slug=slug)

    rooms = Room.objects.filter(hotel=hotel).order_by('category').all()

    categories = dict((k, list(g)) for k, g in groupby(rooms, key=lambda x: x.category))

    # bring all images of hotel
    image_list = hotel.images.all()

    data = {
        'hotel': hotel,
        'image_list': image_list,
        'categories': categories
    }

    return render(request, 'hotels/hotel.html', data)
