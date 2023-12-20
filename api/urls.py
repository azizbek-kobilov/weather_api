from django.urls import path
from api.views import WeatherDetail

app_name = 'api'

urlpatterns = [
    path('', WeatherDetail.as_view(), name='weather_detail'),
]
