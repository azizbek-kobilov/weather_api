from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    weather_keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Узнать погоду")]], resize_keyboard=True
    )

    await message.answer(
        text='Привет, {first_name}!'.format(first_name=message.from_user.first_name),
        reply_markup=weather_keyboard
    )

    await state.finish()
