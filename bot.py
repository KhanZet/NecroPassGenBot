from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.client.default import DefaultBotProperties


from modules import json_tools as jt

from handlers import (
    bot_commands,
    bot_messages,
    settings,
    account,
    help_info,
    market,
    password_gen,
    tools,
)

API_TOKEN = ""


bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
router = Router()


async def on_startup():
    print("Бот запущен")
    print(jt.user_data_path)


if __name__ == "__main__":
    dp.include_routers(
        router,
        account.router,
        settings.router,
        help_info.router,
        market.router,
        password_gen.router,
        tools.router,
        bot_commands.router,
        bot_messages.router,
    )
    dp.startup.register(on_startup)
    dp.run_polling(bot)
