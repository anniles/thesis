from django import template
from ..models import Hotel

register = template.Library()

@register.inclusion_tag('hotels/hotel_snippet.html')
def render_three_random_hotels():
    hotels = Hotel.objects.all().order_by('?')[:3]
    return {'hotels': hotels}

@register.filter
def rangestar(value):
    xs = ""
    for x in range(0, abs(value)):
        xs+="x"
    return xs
