from django.contrib import admin

from .models import Booking, Participant

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_filter = ["confirmed"]
    list_display = ["event", "participant", "booking_date", "confirmed"]
    readonly_fields = ["booking_date"]


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    prepopulated_fields = {"full_name": ["first_name", "last_name"]}


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Booking, BookingAdmin)
