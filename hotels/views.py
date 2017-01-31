from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django import template

from .models import Hotel
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

    # bring all images of hotel
    property = Hotel.objects.get(id=hotel.id)
    image_list = property.images.all()

    data = {
        'hotel': hotel,
        'image_list': image_list,
    }

    return render(request, 'hotels/hotel.html', data)
