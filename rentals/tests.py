from django.test import TestCase
from django.urls import reverse

from .models import Rental, Car, Bike

# Create your tests here.
def create_rental():

    rental1 = Rental.objects.create(slug='rental1', name='rental1', address='rental1', phone='rental1', description='rental1')
    rental2 = Rental.objects.create(slug='rental2', name='rental2', address='rental2', phone='rental2', description='rental2')

    return (rental1, rental2)


class RentalViewTest(TestCase):
    
    def test_index_view_whith_no_cars(self):

        response = self.client.get(reverse('rentals:cars'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Car's available.")
        self.assertQuerysetEqual(response.context['cars'], [])

    def test_index_view_whith_no_bikes(self):

        response = self.client.get(reverse('rentals:bikes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Bike's available.")
        self.assertQuerysetEqual(response.context['bikes'], [])

    def test_index_view_whith_cars(self):

        rental1, rental2 = create_rental()
        rental1.car_set.create(
            slug='car1',
            cc='1100',
            plate='AK234',
            description='cars 1',
            category='SUV',
            model='suzuki'
            )
        rental2.car_set.create(
            slug='car2',
            cc='1300',
            plate='BA234',
            description='cars 2',
            category='SUV',
            model='jeep'
            )
        response = self.client.get(reverse('rentals:cars'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cars'], ['<Car: jeep>', '<Car: suzuki>'])

    def test_index_view_whith_bikes(self):

        rental1, rental2 = create_rental()
        rental1.bike_set.create(
            slug='bike1',
            cc='1100',
            plate='AK234',
            description='bike 1',
            category='cruiser',
            model='tenere'
            )
        rental1.car_set.create(
            slug='car2',
            cc='1300',
            plate='BA234',
            description='cars 2',
            category='SUV',
            model='jeep'
            )
        response = self.client.get(reverse('rentals:bikes'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['bikes'], ['<Bike: tenere>'])
