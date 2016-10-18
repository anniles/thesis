from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Hotel
from django import template


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'hotels/index.html'
    context_object_name = 'hotels'

    def get_queryset(self):
        return Hotel.objects.order_by('name').all()


class DetailView(generic.DetailView):
    model = Hotel
    template_name = 'hotels/hotel.html'


