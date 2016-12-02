from django.test import TestCase
from django.urls import reverse

from .models import Hotel

# Create your tests here.
def create_hotel(slug, name, address, phone, description, category):
    return Hotel.objects.create(slug=slug, name=name, address=address, phone=phone, description=description, category=category)


class HotelViewTest(TestCase):
    
    def test_index_view_whith_no_hotels(self):

        response = self.client.get(reverse('hotels:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hotel's available.")
        self.assertQuerysetEqual(response.context['hotels'], [])

    def test_index_view_whith_hotels(self):

        create_hotel("hotel-1","hotel 1","a","b","c","3")
        create_hotel("hotel-2","hotel 2","a","b","c","1")
        
        response = self.client.get(reverse('hotels:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['hotels'], ['<Hotel: hotel 1>','<Hotel: hotel 2>'])

    def test_index_view_with_category_filter(self):
        
        create_hotel("hotel-1","hotel 1","a","b","c","3")
        create_hotel("hotel-2","hotel 2","a","b","c","2")

        response = self.client.get("%s?c=2" % (reverse('hotels:index'),))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['hotels'], ['<Hotel: hotel 2>'])

        response = self.client.get("%s?c=2&c=3" % (reverse('hotels:index'),))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['hotels'], ['<Hotel: hotel 1>','<Hotel: hotel 2>'])

    def test_detail_view_with_no_existing_hotel(self):

        create_hotel("hotel-1","hotel 1","a","b","c","3")
        
        response = self.client.get(reverse('hotels:detail', kwargs={'slug': 'hotel-2'}))
        self.assertEqual(response.status_code, 404)
    
    def test_detail_view_with_hotel(self):

        hotel = create_hotel("hotel-1","hotel 1","a","b","c","3")

        
        response = self.client.get(reverse('hotels:detail', kwargs={'slug': 'hotel-1'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, hotel.description)
