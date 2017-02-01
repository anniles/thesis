from django.db import models
from django.contrib import admin


# Create your models here.
class Amenity(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    CATEGORY_CHOICES = (
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    )

    slug = models.SlugField(max_length=40)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    category = models.SmallIntegerField(
        choices=CATEGORY_CHOICES,
        default=1,
    )
    description = models.TextField(default='' , null=True)
    image = models.ImageField(upload_to = 'hotel_image', blank=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    property = models.ForeignKey(Hotel, related_name='images')
    image = models.ImageField(upload_to = 'hotel_image', blank=True)

    def __str__(self):
        return self.image.url


class RoomType(models.Model):

    TYPE_CHOICES = (
        ('RO', 'Room only'),
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Half Board (Breakfast and Dinner)'),
        ('FB', 'Full Board (Beakfast, Lunch and Dinner)'),
        ('AI', 'All Inclusive'),
    )

    roomtype = models.CharField(
        choices=TYPE_CHOICES,
        default='RO',
        max_length=2,
    )
    coefficient = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)

    def __str__(self):
        return self.roomtype


class Room(models.Model):
    CATEGORY_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    roomtype = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    max_guest = models.PositiveSmallIntegerField()
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default='single',
        max_length=200,
    )
    description = models.TextField(default='' , null=True)
    amenities = models.ManyToManyField(Amenity)
    # image = models.ImageField(upload_to = 'room_image', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return "{}_{}_{}".format(self.id, self.category, self.hotel)


class RoomImage(models.Model):
    property = models.ForeignKey(Room, related_name='images')
    image = models.ImageField(upload_to = 'room_image', blank=True)

    def __str__(self):
        return "{}_{}".format(self.property, self.image.url)