from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Sight


# Create your views here.
def index(request):

    sights = Sight.objects.order_by('name').all()

    data = {
        'active_tab': 'sights',
        'sights': sights
    }

    return render(request, 'sights/index.html', data)


def detail(request, slug):

    sight = get_object_or_404(Sight, slug=slug)

    # bring all images of sight
    property = Sight.objects.get(id=sight.id)
    image_list = property.images.all()

    data = {
        'sight': sight,
        'image_list': image_list,
        'active_tab': 'sights',
    }

    return render(request, 'sights/detail.html', data)