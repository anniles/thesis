from django.db import models
from django.contrib import admin


# Create your models here.
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

	def __str__(self):
		return self.name


class RoomType(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	
	def __str__(self):
		return self.name


class Room(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	roomtype = models.ForeignKey(RoomType, on_delete=models.CASCADE)
	max_guest = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'ulpoads', default = 'static/tourguide/images/pic_folder/None/no-img.jpg' , null=True)
	description = models.TextField(default='' , null=True)

	def __str__(self):
		return self.title
