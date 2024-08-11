from aiogram import Router, F
from aiogram.types import Message

from keyboards.reply import main

router = Router()


@router.message()
async def echo(message: Message):
    await message.answer("Вы возращены в главное меню...", reply_markup=main)
