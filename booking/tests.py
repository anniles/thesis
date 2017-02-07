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


class CarViewsTest(TestCase):

    fixtures = ['rentals.yaml', 'users.yaml']

    def test_car_index_view_when_no_booked_cars(self):
        checkin = '2017-02-02'
        checkout = '2017-02-07'

        response = self.client.get("%s?checkin=%s&checkout=%s" % (reverse('booking:search_car'), checkin, checkout))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [
            '<Car: 1_Hyundai atos_Sixt>',
            '<Car: 3_Hyundai getz_Sixt>',
            '<Car: 2_suzuki swift_Evros Car Rental>'
        ])

    def test_car_index_view_when_one_booked_cars(self):
        # fetch data
        user = User.objects.get(pk=10)
        car  = BookCar.objects.get(pk=1)
        car2  = BookCar.objects.get(pk=2)
        car3  = BookCar.objects.get(pk=3)

        # searching dates
        checkin = '2017-02-02'
        checkout = '2017-02-06'

        # create booking for user
        booking = Booking(user=user)
        booking.save()

        # booked dates for a car
        bookingItem = BookingItem(
            content_object=car,
            booking=booking,
            check_in=date(2017,2,2),
            check_out=date(2017,2,7),
            price=car.price
        )

        bookingItem.save()

        # test response
        response = self.client.get("%s?checkin=%s&checkout=%s" %
            (reverse('booking:search_car'), checkin, checkout))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [
            '<Car: 3_Hyundai getz_Sixt>',
            '<Car: 2_suzuki swift_Evros Car Rental>'
        ])

        # booked dates for car and car2
        bookingItem = BookingItem(
            content_object=car2,
            booking=booking,
            check_in=date(2017,2,2),
            check_out=date(2017,2,7),
            price=car.price
        )

        bookingItem.save()

        # test response
        response = self.client.get("%s?checkin=%s&checkout=%s" %
            (reverse('booking:search_car'), checkin, checkout))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [
            '<Car: 3_Hyundai getz_Sixt>',
        ])

        # booked car3 before test dates
        bookingItem = BookingItem(
            content_object=car3,
            booking=booking,
            check_in=date(2017,1,2),
            check_out=date(2017,1,7),
            price=car.price
        )

        bookingItem.save()

        response = self.client.get("%s?checkin=%s&checkout=%s" %
           (reverse('booking:search_car'), checkin, checkout))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [
            '<Car: 3_Hyundai getz_Sixt>',
        ])

        # booked all cars for same dates
        bookingItem = BookingItem(
            content_object=car3,
            booking=booking,
            check_in=date(2017,2,2),
            check_out=date(2017,2,7),
            price=car.price
        )

        bookingItem.save()

        response = self.client.get("%s?checkin=%s&checkout=%s" %
           (reverse('booking:search_car'), checkin, checkout))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], [])
