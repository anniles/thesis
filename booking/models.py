from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Q

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from hotels.models import Room
from rentals.models import Car, Bike

from registration.signals import user_registered
from django.dispatch import receiver


class BookingContact(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.email


class Booking(models.Model):
    user = models.ForeignKey(BookingContact, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class BookingItem(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id', for_concrete_model=True)

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now=False, auto_now_add=False)
    check_out = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class BookRoom(Room):

    def add_item(self, booking, dates):

        bookingItem = BookingItem(content_object=self,
                booking=booking,
                check_in=dates["checkin"],
                check_out=dates["checkout"],
                price=self.price)

        bookingItem.save()

    # check if room is available on wanted dates
    def is_available(self, check_in, check_out):

        room_content_type = ContentType.objects.get_for_model(self)

        count = BookingItem.objects.filter(
            (Q(check_in__gte=check_in) & Q(check_in__lte=check_out)) |
            (Q(check_out__gte=check_in) & Q(check_out__lte=check_out)) |
            (Q(check_in__lte=check_in) & Q(check_out__gte=check_out)),
            Q(content_type__pk=room_content_type.id) & Q(object_id=self.id)
            ).count()

        return False if count>0 else True

    class Meta:
        proxy = True


class BookCar(Car):

    def add_item(self, booking, dates):

        bookingItem = BookingItem(content_object=self,
                booking=booking,
                check_in=dates["checkin"],
                check_out=dates["checkout"],
                price=self.price)

        bookingItem.save()

    # check if car is available on wanted dates
    def is_available(self, check_in, check_out):

        car_content_type = ContentType.objects.get_for_model(self)

        count = BookingItem.objects.filter(
            (Q(check_in__gte=check_in) & Q(check_in__lte=check_out)) |
            (Q(check_out__gte=check_in) & Q(check_out__lte=check_out)) |
            (Q(check_in__lte=check_in) & Q(check_out__gte=check_out)),
            Q(content_type__pk=car_content_type.id) & Q(object_id=self.id)
            ).count()

        return False if count>0 else True

    class Meta:
        proxy = True


class BookBike(Bike):

    def add_item(self, booking, dates):

        bookingItem = BookingItem(content_object=self,
                booking=booking,
                check_in=dates["checkin"],
                check_out=dates["checkout"],
                price=self.price)

        bookingItem.save()

    # check if bike is available on wanted dates
    def is_available(self, check_in, check_out):

        bike_content_type = ContentType.objects.get_for_model(self)

        count = BookingItem.objects.filter(
            (Q(check_in__gte=check_in) & Q(check_in__lte=check_out)) |
            (Q(check_out__gte=check_in) & Q(check_out__lte=check_out)) |
            (Q(check_in__lte=check_in) & Q(check_out__gte=check_out)),
            Q(content_type__pk=bike_content_type.id) & Q(object_id=self.id)
            ).count()

        return False if count>0 else True

    class Meta:
        proxy = True


# upon register we want to connect the user to a client who has bookings
# we do that by cross checking emails
@receiver(user_registered)
def create_client(sender, user, **kwargs):
    try:
        client = BookingContact.objects.filter(email=user.email).update(user=user)
    except Exception as e:
        print (str(e))

