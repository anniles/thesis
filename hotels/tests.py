from django.test import TestCase
from django.urls import reverse

from .models import Hotel

# Create your tests here.
def create_hotel(slug, name, address, phone, description):
    return Hotel.objects.create(slug=slug, name=name, address=address, phone=phone, description=description)


class HotelViewTest(TestCase):
    
    def test_index_view_whith_no_hotels(self):

        response = self.client.get(reverse('hotels:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hotel's available.")
        self.assertQuerysetEqual(response.context['hotels'], [])

    def test_index_view_whith_hotels(self):

        create_hotel("hotel-1","hotel 1","a","b","c")
        response = self.client.get(reverse('hotels:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['hotels'], ['<Hotel: hotel 1>'])
