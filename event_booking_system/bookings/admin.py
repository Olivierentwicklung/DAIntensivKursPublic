from django.contrib import admin

from .models import Booking, Participant

# Register your models here.
admin.site.register(Participant)
admin.site.register(Booking)
