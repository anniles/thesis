from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user.username


class BookingItem(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now=False, auto_now_add=False)
    check_out = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # def __str__(self):
        # return self.content_type
        
