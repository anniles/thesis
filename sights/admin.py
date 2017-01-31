from django.contrib import admin
from .models import Sight, SightImage

# Register your models here.

class SightImageInline(admin.TabularInline):
    model = SightImage
    extra = 0


class SightAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",) }
    inlines = [SightImageInline, ]

    def short_description(self, obj):
        return obj.description[:100]


admin.site.register(Sight, SightAdmin)