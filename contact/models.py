from django.db import models
from django.contrib import admin


# Create your models here.


class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    message = models.TextField()
    
    def __str__(self):
        return self.email