from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile

from utils.states import Account_form

from keyboards.builders import any_kb
from keyboards.reply import rmk, my_account_kb, main

from modules import json_tools as jt

router = Router()


@router.message(F.text == "👤 Мой Кабинет")
async def my_account(message: Message, state: FSMContext):
    await message.answer(
        f"🆔 Идентификатор пользователя: {message.from_user.id} \n\n"
        f"Интересненько...",
        reply_markup=my_account_kb,
    )
    await state.set_state(Account_form.start_menu)


@router.message(F.text == "📚 Моя история")
async def send_history(message: Message):
    user_id = message.from_user.id
    users_data = jt.read_json(jt.user_data_path)
    user_data = jt.find_user_by_id(users_data, user_id)

    history_path = "history.txt"
    with open(history_path, "w") as f:
        for date, passwords in user_data["history"].items():
            f.write(f"{date}:\n")
            for password in passwords:
                f.write(f"  {password}\n")
            f.write("\n")

    await message.answer_document(FSInputFile(history_path))


@router.message(Account_form.start_menu, F.text == "🔙 Назад")
async def back_to_menu(message: Message, state: FSMContext):
    await message.answer("Переход к главному меню...", reply_markup=main)
    await state.clear()
