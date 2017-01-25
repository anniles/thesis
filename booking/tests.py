from django.test import TestCase
from django.urls import reverse

from hotels.models import Hotel, Room

from .models import Booking, BookingItem


class RoomAvailabilityTest(TestCase):
    fixtures = ['hotels.yaml']
    
    def test_availability_when_no_bookings(self):
        room = Room.objects.get(pk=1)

        self.assertEqual(room.is_available(), True)

# Create your tests here.
# class BookingRoomSearchViewTest(TestCase):
#     # hotels count 4
#     # rooms count  7
#     fixtures = ['hotels.yaml']
    
#     def test_search_when_no_bookings(self):

#         response = self.client.get(reverse('booking:search_hotel'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context['results']), 4)

