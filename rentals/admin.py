from django.contrib import admin
from .models import Rental, Car, Bike


# not working
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("model","cc") }


# not working
class BikeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("model","cc") }


class CarInline(admin.StackedInline):
    model = Car
    extra = 0


class BikeInline(admin.StackedInline):
    model = Bike
    extra = 0


class RentalAdmin(admin.ModelAdmin):
    #slug is the name of the hotel that appears in the url hyphen(/) seperated and lowercase
    prepopulated_fields = {"slug": ("name",) }
    inlines = [
        CarInline,
        BikeInline,
    ]


# Register your models here.
admin.site.register(Rental, RentalAdmin)
# admin.site.register(Bike, BikeAdmin)
# admin.site.register(Car, CarAdmin)
