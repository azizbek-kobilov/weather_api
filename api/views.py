import json
from datetime import timedelta
from django.utils import timezone
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import WeatherData
from .utils import get_city_coords, get_weather_data


class WeatherDetail(APIView):
    serializer_class = None
    def get(self, request):
        city_name = request.GET.get('city', None)
        if not city_name:
            return JsonResponse({'error': 'City name is required.'}, status=400)

        try:
            city_coords = get_city_coords(city_name)
            if city_coords is None:
                return JsonResponse({'error': 'Failed to get city.'}, status=400)

            latitude = city_coords['latitude']
            longitude = city_coords['longitude']

            weather_data = WeatherData.objects.filter(city=city_name).first()
            if weather_data and timezone.now() - weather_data.modified < timedelta(minutes=30):
                return JsonResponse(json.loads(weather_data.data))

            weather_data = get_weather_data(latitude, longitude)

            data = {
                'temperature': weather_data['fact']['temp'],
                'pressure': weather_data['fact']['pressure_mm'],
                'wind_speed': weather_data['fact']['wind_speed'],
            }
            weather_info, _ = WeatherData.objects.update_or_create(
                city=city_name,
                defaults={'data': json.dumps(data)}
            )

            return JsonResponse(data)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
