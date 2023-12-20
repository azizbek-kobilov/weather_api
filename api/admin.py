from django.contrib import admin
from api.models import WeatherData


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'modified')
