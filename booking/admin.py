from django.contrib import admin
from .models import Booking, BookingItem

# Register your models here.
class BookingItemInline(admin.StackedInline):
    model = BookingItem
    extra = 0


class BookingAdmin(admin.ModelAdmin):
    inlines = [BookingItemInline]
    list_display = ('created_at','user','updated_at')


admin.site.register(Booking, BookingAdmin)