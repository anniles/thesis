from django import template
from ..models import Hotel

register = template.Library()

@register.inclusion_tag('hotels/hotel_snippet.html')
def render_three_random_hotels():
	hotels = Hotel.objects.all()[:3]
	return {'hotels': hotels}

