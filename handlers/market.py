from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.builders import any_kb
from keyboards.reply import rmk, my_account_kb


router = Router()


@router.message((F.text == "💸 Магазин") | (F.text == "/market"))
async def market(message: Message):
    await message.answer("Мы новенькие. Все бесплатно :3")
