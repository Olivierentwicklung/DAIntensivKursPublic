from django.contrib import admin

from .models import Event, EventCategory, Location

# Register your models here.
admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event)
