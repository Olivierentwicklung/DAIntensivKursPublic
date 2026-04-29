from django.contrib import admin

from .models import Event, EventCategory, Location

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]


admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event, EventAdmin)
