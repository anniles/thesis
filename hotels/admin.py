from django.contrib import admin
from .models import Hotel


class HotelAdmin(admin.ModelAdmin):
	#slug is the name of the hotel that appears in the url hyphen(/) seperated and lowercase
	prepopulated_fields = {"slug": ("name",) }


# Register your models here.
admin.site.register(Hotel, HotelAdmin)