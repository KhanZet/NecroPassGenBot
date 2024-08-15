from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.builders import any_kb
from keyboards.reply import rmk, my_account_kb

from modules import pass_gen as pg
from datetime import datetime as dt
from modules import json_tools as jt

import html


router = Router()


@router.message(F.text == "🔐 Сгенерировать пароль")
async def pass_gen(message: Message):
    user_id = message.from_user.id

    # Загружаем настройки пользователей
    users_settings = jt.read_json(jt.user_settings_path)
    user_from_settings = jt.find_user_by_id(users_settings, user_id)

    # Если пользователь не найден в настройках, создаем его
    if not user_from_settings:
        jt.create_user(user_id, message.from_user.username)
        users_settings = jt.read_json(jt.user_settings_path)
        user_from_settings = jt.find_user_by_id(users_settings, user_id)

    # Генерация пароля
    password = pg.generate_password(user_from_settings)
    safe_password = html.escape(password)

    # Загружаем данные пользователей
    users_data = jt.read_json(jt.user_data_path)
    user_data = jt.find_user_by_id(users_data, user_id)
    time = dt.now().strftime("%d%m%Y")

    # Если пользователь не найден в данных, создаем его
    if not user_data:
        new_user = {
            "user_id": user_id,
            "username": message.from_user.username,
            "history": {time: [safe_password]},
        }
        users_data.append(new_user)
        user_data = new_user  # Теперь user_data ссылается на новый объект
    else:
        jt.add_password(user_data, time, safe_password)

    # Запись обновленных данных
    jt.write_json(users_data, jt.user_data_path)

    # Отправка пароля пользователю
    await message.answer(f"<code>{safe_password}</code>", parse_mode="HTML")


# test
