from django.contrib import admin
from .models import Location
from .models import Weather

admin.site.register(Location)
admin.site.register(Weather)
