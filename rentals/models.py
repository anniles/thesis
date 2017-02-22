from django.db import models
from django.contrib import admin


# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    description = models.TextField(default="", null=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_CATEGORY = (
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Sedan', 'Sedan'),
        ('Van', 'Van'),
        ('Coupe/Compact', 'Coupe/Compact'),
        ('Wagon', 'Wagon'),
        ('Convertible', 'Convertible'),
        ('Sports Car', 'Sports Car'),
        ('Diesel', 'Diesel'),
        ('Crossover', 'Crossover'),
        ('Luxury Car', 'Luxury Car'),
        ('Hybrid/Electric', 'Hybrid/Electric'),
        ('Hatchback', 'Hatchback'),
    )

    model = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    cc = models.CharField(max_length=50)
    plate = models.CharField(max_length=20)
    description = models.TextField(default="", null=True)
    category = models.CharField(
        choices=CAR_CATEGORY,
        default='',
        max_length=200,
    )
    image = models.ImageField(upload_to = 'car_image', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "{}_{}_{}".format(self.id, self.model, self.rental)


class CarImage(models.Model):
    property = models.ForeignKey(Car, related_name='images')
    image = models.ImageField(upload_to = 'car_image', blank=True)

    def __str__(self):
        return "{}_{}".format(self.property, self.image.url)


class Bike(models.Model):
    BIKE_CATEGORY = (
        ('Standard', 'Standard'),
        ('Cruiser', 'Cruiser'),
        ('Sport bike', 'Sport bike'),
        ('Touring', 'Touring'),
        ('Sport touring', 'Sport touring'),
        ('Dual-sport', 'Dual-sport'),
        ('Scooters', 'Scooters'),
        ('Off-road', 'Off-road'),
        ('Enclosed', 'Enclosed'),
        ('Utility', 'Utility'),
        ('Tricycles', 'Tricycles'),
    )

    model = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    cc = models.CharField(max_length=50)
    plate = models.CharField(max_length=20)
    description = models.TextField(default="", null=True)
    category = models.CharField(
        choices=BIKE_CATEGORY,
        default='',
        max_length=200,
    )
    image = models.ImageField(upload_to = 'bike_image', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "{}_{}_{}".format(self.id, self.model, self.rental)


class BikeImage(models.Model):
    property = models.ForeignKey(Bike, related_name='images')
    image = models.ImageField(upload_to = 'bike_image', blank=True)

    def __str__(self):
        return "{}_{}".format(self.property, self.image.url)
