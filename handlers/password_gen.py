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
    user_from_settings = jt.find_user_by_id(jt.user_settings_path, user_id)
    password = pg.generate_password(user_from_settings)
    safe_password = html.escape(password)
    users_data = jt.read_json(jt.user_data_path)
    user_data = jt.find_user_by_id(users_data, user_id)
    time = dt.now().strftime("%d%m%Y")

    if user_data:
        jt.add_password(user_data, time, safe_password)
    else:
        new_user = {
            "user_id": user_id,
            "username": message.from_user.username,
            "history": {time: [safe_password]},
        }
        users_data.append(new_user)
    jt.write_json(users_data, jt.user_data_path)

    await message.answer(f"<code>{safe_password}</code>", parse_mode="HTML")


# test
