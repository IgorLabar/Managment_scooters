from django.contrib import admin
from .models import Scooter, Trip


class ScooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'active')
    search_fields = ('serial_number',)


class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'cost', 'date_of_trip', 'rider')
    search_fields = ('date_of_trip',)
    list_filter = ('cost',)


admin.site.register(Scooter, ScooterAdmin)
admin.site.register(Trip, TripAdmin)
