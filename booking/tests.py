from datetime import date

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Booking, BookingItem, BookRoom, BookCar, BookBike


class RoomAvailabilityTest(TestCase):

    fixtures = ['hotels.yaml', 'users.yaml']
    
    def setUp(self):
        self.user = User.objects.get(pk=10)
        self.room = BookRoom.objects.get(pk=1)
        # print(self.user)

    def test_availability_when_no_bookings(self):

        self.assertEqual(self.room.is_available(date(2017,1,10), date(2017,1,15)), True)

    def test_availability_with_different_dates_when_booked(self):
        
        booking = Booking(user=self.user)
        booking.save()

        bookingItem = BookingItem(content_object=self.room, booking=booking, check_in=date(2017,1,1), check_out=date(2017,1,8), price=self.room.price)
        bookingItem.save()

        #search on dates after bookings
        self.assertEqual(self.room.is_available(date(2017,1,10), date(2017,1,15)), True)
        #search on dates in the middle of bookings
        self.assertEqual(self.room.is_available(date(2017,1,7), date(2017,1,15)), False)
        #search on dates exactly same dates of bookings
        self.assertEqual(self.room.is_available(date(2017,1,1), date(2017,1,8)), False)
        #search on dates before of bookings
        self.assertEqual(self.room.is_available(date(2016,1,1), date(2016,1,8)), True)
        #search on dates between of bookings
        self.assertEqual(self.room.is_available(date(2017,1,2), date(2017,1,6)), False)
 

class CarAvailabilityTest(TestCase):

    fixtures = ['rentals.yaml', 'users.yaml']
    
    def setUp(self):
        self.user = User.objects.get(pk=10)
        self.car = BookCar.objects.get(pk=1)
        # print(self.user)

    def test_availability_when_no_bookings(self):

        self.assertEqual(self.car.is_available(date(2017,1,10), date(2017,1,15)), True)

    def test_availability_with_different_dates_when_booked(self):
        
        booking = Booking(user=self.user)
        booking.save()

        bookingItem = BookingItem(content_object=self.car, booking=booking, check_in=date(2017,1,1), check_out=date(2017,1,8), price=self.car.price)
        bookingItem.save()

        #search on dates after bookings
        self.assertEqual(self.car.is_available(date(2017,1,10), date(2017,1,15)), True)
        #search on dates in the middle of bookings
        self.assertEqual(self.car.is_available(date(2017,1,7), date(2017,1,15)), False)
        #search on dates exactly same dates of bookings
        self.assertEqual(self.car.is_available(date(2017,1,1), date(2017,1,8)), False)
        #search on dates before of bookings
        self.assertEqual(self.car.is_available(date(2016,1,1), date(2016,1,8)), True)
        #search on dates between of bookings
        self.assertEqual(self.car.is_available(date(2017,1,2), date(2017,1,6)), False)        


class BikeAvailabilityTest(TestCase):

    fixtures = ['rentals.yaml', 'users.yaml']
    
    def setUp(self):
        self.user = User.objects.get(pk=10)
        self.bike = BookBike.objects.get(pk=1)
        # print(self.user)

    def test_availability_when_no_bookings(self):

        self.assertEqual(self.bike.is_available(date(2017,1,10), date(2017,1,15)), True)

    def test_availability_with_different_dates_when_booked(self):
        
        booking = Booking(user=self.user)
        booking.save()

        bookingItem = BookingItem(content_object=self.bike, booking=booking, check_in=date(2017,1,1), check_out=date(2017,1,8), price=self.bike.price)
        bookingItem.save()

        #search on dates after bookings
        self.assertEqual(self.bike.is_available(date(2017,1,10), date(2017,1,15)), True)
        #search on dates in the middle of bookings
        self.assertEqual(self.bike.is_available(date(2017,1,7), date(2017,1,15)), False)
        #search on dates exactly same dates of bookings
        self.assertEqual(self.bike.is_available(date(2017,1,1), date(2017,1,8)), False)
        #search on dates before of bookings
        self.assertEqual(self.bike.is_available(date(2016,1,1), date(2016,1,8)), True)
        #search on dates between of bookings
        self.assertEqual(self.bike.is_available(date(2017,1,2), date(2017,1,6)), False)




# Create your tests here.
# class BookingRoomSearchViewTest(TestCase):
#     # hotels count 4
#     # rooms count  7
#     fixtures = ['hotels.yaml']
    
#     def test_search_when_no_bookings(self):

#         response = self.client.get(reverse('booking:search_hotel'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context['results']), 4)

