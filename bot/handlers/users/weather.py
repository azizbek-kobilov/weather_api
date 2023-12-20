from aiogram import types
from aiogram.dispatcher import FSMContext
from api.utils import get_city_coords, get_weather_data
from bot.states import Weather
from loader import dp


@dp.message_handler(text="Узнать погоду")
async def weather(message: types.Message):
    await Weather.city.set()
    await message.answer(text='Введите название города')


@dp.message_handler(state=Weather.city)
async def city(message: types.Message, state: FSMContext):
    city_coords = get_city_coords(message.text)
    if city_coords is None:
        await message.answer(text='Не удалось определить город, попробуйте еще раз')
        return

    try:
        weather_data = get_weather_data(city_coords['latitude'], city_coords['longitude'])
        forecast_message = f'Температура: {weather_data["fact"]["temp"]}\n' \
                           f'Давление: {weather_data["fact"]["pressure_mm"]}\n' \
                           f'Скорость ветра: {weather_data["fact"]["wind_speed"]}'
        await message.answer(forecast_message)
    except Exception as e:
        await message.answer('Не удалось получить данные о погоде, попробуйте позже')
    finally:
        await state.finish()
