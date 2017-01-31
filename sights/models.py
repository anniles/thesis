from django.db import models

# Create your models here.
class Sight(models.Model):

    slug = models.SlugField(max_length=40)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(default='' , null=True)
    image = models.ImageField(upload_to = 'sight_image', blank=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.name

class SightImage(models.Model):
    property = models.ForeignKey(Sight, related_name='images')
    image = models.ImageField(upload_to = 'sight_image', blank=True)

    def __str__(self):
        return self.image.url