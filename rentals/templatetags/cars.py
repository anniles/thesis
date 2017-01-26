from django import template
from ..models import Car

register = template.Library()

@register.inclusion_tag('rentals/car_snippet.html')
def render_three_random_cars():
    cars = Car.objects.all()[:3]
    return {'cars': cars}