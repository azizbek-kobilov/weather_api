from django.core.management.base import BaseCommand
from aiogram import executor
from loader import dp
from bot.handlers import *
from bot import middlewares
from bot.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    middlewares.setup(dispatcher)


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        executor.start_polling(dp, on_startup=on_startup)
