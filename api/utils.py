import requests
from config.settings import YANDEX_KEY


def get_city_coords(city_name):
    city_name_url = f'https://nominatim.openstreetmap.org/search?q={city_name}&format=json&addressdetails=1&limit=1'
    response = requests.get(city_name_url)
    if response.status_code != 200 or not response.json():
        return None
    geocoding_data = response.json()[0]
    data = {
        'latitude': geocoding_data['lat'],
        'longitude': geocoding_data['lon']
    }
    return data


def get_weather_data(latitude, longitude):
    yandex_response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}',
                                   headers={'X-Yandex-API-Key': YANDEX_KEY})
    yandex_response.raise_for_status()
    weather_data = yandex_response.json()
    return weather_data
