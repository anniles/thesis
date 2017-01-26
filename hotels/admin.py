from django.contrib import admin
from .models import Hotel, RoomType, Room, Amenity, HotelImage


class RoomInline(admin.StackedInline):
    model = Room
    extra = 1


class RoomTypeInline(admin.TabularInline):
    model = RoomType


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 2


class HotelAdmin(admin.ModelAdmin):
    #slug is the name of the hotel that appears in the url hyphen(/) seperated and lowercase
    prepopulated_fields = {"slug": ("name",) }
    inlines = [RoomInline, HotelImageInline]
    list_display = ('name', 'address', 'phone', 'category', 'short_description')

    def short_description(self, obj):
        return obj.description[:100] 



# Register your models here.
admin.site.register(Hotel, HotelAdmin)
# admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Amenity)