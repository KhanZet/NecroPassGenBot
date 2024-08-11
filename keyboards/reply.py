from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 Мой Кабинет"), KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="💸 Магазин"), KeyboardButton(text="❓ Помощь")],
        [KeyboardButton(text="🔐 Сгенерировать пароль")],
        [KeyboardButton(text="🔧 Инструменты")],
    ],
    resize_keyboard=True,
)

configure_settings_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ]
)

rmk = ReplyKeyboardRemove()

configure_settings_kb_fixed_length = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6")],
        [KeyboardButton(text="🔙 Назад")],
    ]
)

my_account_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📚 Моя история"), KeyboardButton(text="🔙 Назад")]],
    resize_keyboard=True,
)

tools_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Случайное число"),
            KeyboardButton(text="Случайное Эмодзи"),
        ],
        [KeyboardButton(text="Случайный польский мат")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
)
