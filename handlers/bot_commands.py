from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message


from modules import json_tools as jt

from keyboards import reply

router = Router()


@router.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Приветствую повелителя", reply_markup=reply.main)
    user_id = message.from_user.id
    user_data = {
        "user_id": user_id,
        "username": message.from_user.username,
        "history": {},
    }
    user_settings = {
        "user_id": user_id,
        "password_settings": {
            "length": {
                "min_length": 8,
                "max_length": 16,
                "total_length": 15,
                "fixed_length": True,
            },
            "include_uppercase": True,
            "include_lowercase": True,
            "include_digits": True,
            "include_specials": True,
        },
    }

    if jt.find_user_by_id(jt.read_json(jt.user_data_path), user_id):
        print("Данные пользователя есть в базе")
    else:
        jt.add_user(user_data, jt.user_data_path)

    if jt.find_user_by_id(jt.read_json(jt.user_settings_path), user_id):
        print("Настройки пользователя есть в базе")
    else:
        jt.add_user(user_settings, jt.user_settings_path)


@router.message(Command("generate"))
async def pass_gen(message: Message):
    await message.answer("Password has been generated")
