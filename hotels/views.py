from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Hotel
from django import template


# Create your views here.
def index(request):
	#take all hotels from db order by name
	hotels = Hotel.objects.order_by('name').all()
	template = loader.get_template('hotels/index.html')
	data = {
		'hotels': hotels
	}
	return HttpResponse(template.render(data, request))


