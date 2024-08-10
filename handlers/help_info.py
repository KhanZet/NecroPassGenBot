from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()


@router.message((F.text == "/help") | (F.text == "❓ Помощь"))
async def help(message: Message):
    await message.answer(
        "<b><i>Добро пожаловать в NecroPassGenBot!</i></b> Этот бот поможет вам сгенерировать надежные пароли. Вот как вы можете использовать его:\n\n"
        "<b>1. Заглавные буквы:</b> Вы можете включить или исключить заглавные буквы в вашем пароле.\n\n"
        "<b>2. Строчные буквы:</b> Вы можете включить или исключить строчные буквы в вашем пароле.\n\n"
        "<b>3. Цифры:</b> Вы можете включить или исключить цифры в вашем пароле.\n\n"
        "<b>4. Символы:</b> Вы можете включить или исключить специальные символы в вашем пароле.\n\n"
        "<b>5. Длина пароля:</b> Вы можете задать диапазон длины пароля или указать статичную длину.",
        parse_mode="HTML",
    )
