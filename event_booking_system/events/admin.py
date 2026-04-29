from django.contrib import admin

from .models import Event, EventCategory, Location

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]
    search_fields = ["title", "date"]
    list_filter = [
        "category",
    ]
    fieldsets = [
        (
            "Allgemein",
            {
                "fields": ["title", "category", "date"],
            },
        ),
        (
            "Organisation",
            {
                "classes": ["collapse"],
                "fields": ["location", "capacity"],
            },
        ),
    ]


admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event, EventAdmin)
