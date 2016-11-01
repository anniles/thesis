from django.contrib import admin
from .models import Hotel, RoomType, Room, Amenity


class RoomInline(admin.StackedInline):
    model = Room
    extra = 1


class RoomTypeInline(admin.TabularInline):
    model = RoomType



class HotelAdmin(admin.ModelAdmin):
    #slug is the name of the hotel that appears in the url hyphen(/) seperated and lowercase
    prepopulated_fields = {"slug": ("name",) }
    inlines = [RoomInline]


# Register your models here.
admin.site.register(Hotel, HotelAdmin)
# admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Amenity)