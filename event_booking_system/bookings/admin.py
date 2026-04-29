from django.contrib import admin

from .models import Booking, Participant

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_filter = ["confirmed"]
    list_display = ["event", "participant", "booking_date", "confirmed"]
    readonly_fields = ["booking_date"]


admin.site.register(Participant)
admin.site.register(Booking, BookingAdmin)
