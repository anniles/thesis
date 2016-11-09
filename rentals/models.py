from django.db import models
from django.contrib import admin


# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    description = models.TextField(default="", null=True)
    
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
    #todo price, images

    def __str__(self):
        return self.model


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
    #todo price, images

    def __str__(self):
        return self.model