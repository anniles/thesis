from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Create your views here.
def index(request):


    data = {
        'active_tab': 'transportation',
    }

    return render(request, 'transport/index.html', data)