from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from utils.states import Tools_form

from keyboards.reply import tools_kb, main
from keyboards.builders import any_kb

import random

router = Router()

emoji_string = (
    "😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 "
    "😛 😝 😜 🤪 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹ 😣 "
    "😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 "
    "🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 😴 🤤 😪 😵 😵‍💫 "
    "🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠ 👽 "
    "👾 🤖 😺 😸 😹 😻 😼 😽 🙀 😿 😾 👋 🤚 🖐 ✋ 🖖 👌 🤌 🤏 ✌ 🤞 "
    "🫰 🤟 🤘 🤙 👈 👉 👆 🖕 👇 ☝ 👍 👎 ✊ 👊 🤛 🤜 👏 🙌 🫶 👐 🤲 "
    "🤝 🙏 ✍ 💅 🤳 💪 🦾 🦿 🦵 🦶 👣 👂 🦻 👃 🧠 🦷 🦴 👀 👁 👅 "
    "👄 💋 🩸 👓 🕶 🥽 🦺 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 👙 👚 👛 👜 "
    "👝 🎒 🩴 🩱 🩲 🩳 👞 👟 🥾 🥿 👠 👡 👢 👑 👒 🎩 🎓 🧢 ⛑ "
    "🪖 💄 💍 💼 🪑 🛋 🛏 🛌 🧸 🪆 🖼 🪞 🪟 🛎 🧳 ⌛ ⏳ ⏰ ⏱ ⏲ 🕰 "
    "🕛 🕧 🕐 🕜 🕑 🕝 🕒 🕞 🕓 🕟 🕔 🕠 🕕 🕡 🕖 🕢 🕗 🕣 🕘 🕤 "
    "🕙 🕥 🕚 🕦 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌙 🌚 🌛 🌜 🌡 ☀ 🌝 🌞 "
    "🪐 ⭐ 🌟 🌠 🌌 ☁ ⛅ 🌤 🌥 🌦 🌧 ⛈ 🌩 🌨 🌪 🌫 🌬 🌀 🌈 🌂 ☂ "
    "☔ ⛱ ⚡ ❄ ☃ ⛄ ☄ 🔥 💧 🌊 🎃 🧙‍♀️ 🧙‍♂️ 🧛‍♀️ 🧛‍♂️ 🧜‍♀️ "
    "🧜‍♂️ 🧝‍♀️ 🧝‍♂️ 🧞‍♀️ 🧞‍♂️ 🧟‍♀️ 🧟‍♂️ 🧌 👨‍💻 👩‍💻 🧑‍💻 "
    "👨‍🔧 👩‍🔧 🧑‍🔧 👨‍🔬 👩‍🔬 🧑‍🔬 👨‍🎨 👩‍🎨 🧑‍🎨 👨‍🚀 👩‍🚀 "
    "🧑‍🚀 👨‍🚒 👩‍🚒 🧑‍🚒 🧗‍♀️ 🧗‍♂️ 🧗 🧘‍♀️ 🧘‍♂️ 🧘 🛀 🛌 "
    "💃 🕺 👯‍♀️ 👯‍♂️ 🕴 🚶‍♀️ 🚶‍♂️ 🚶 🏃‍♀️ 🏃‍♂️ 🏃 🦯 🦼 🦽 "
    "🏄‍♀️ 🏄‍♂️ 🏄 🏊‍♀️ 🏊‍♂️ 🏊 🤽‍♀️ 🤽‍♂️ 🤽 🚴‍♀️ 🚴‍♂️ 🚴 🚵‍♀️ "
    "🚵‍♂️ 🚵 🏇 🕴 🏆 🎖 🏅 🥇 🥈 🥉 🏵 🎗 🎫 🎟 🎪 🤹‍♀️ 🤹‍♂️ "
    "🤹 🎨 🎭 🎤 🎧 🎼 🎹 🥁 🎷 🎺 🎸 🪕 🏴‍☠️ 🇺🇳"
)
emoji_string = emoji_string.split()


@router.message(F.text == "🔧 Инструменты")
async def tools_menu(message: Message, state: FSMContext):
    await message.answer("Выберите инструмент: ", reply_markup=tools_kb)
    await state.set_state(Tools_form.start_menu)


@router.message(Tools_form.start_menu)
async def random_int(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await message.answer("Возращение в главное меню", reply_markup=main)
        await state.clear()
    elif message.text == "Случайное число":
        await message.answer(
            "Выберите диапозон (Пример: 1-100)", reply_markup=any_kb(["🔙 Назад"])
        )
        await state.set_state(Tools_form.random_input_value)
    elif message.text == "Случайное Эмодзи":
        emoji = emoji_string[random.randint(0, len(emoji_string))]
        print(len(emoji_string), emoji)
        await message.answer(
            f"<i>Эмодзи</i>  <code>{emoji}</code>\n                   ^\n<b>Копируй нажатием</b>"
        )


@router.message(Tools_form.random_input_value, F.text.regexp(r"^\d+-\d+$"))
async def send_random_int(message: Message, state: FSMContext):
    from_number, to_number = message.text.split("-")
    from_number, to_number = int(from_number), int(to_number)
    if from_number > to_number:
        await message.answer("Левое число, не может быть больше правого")
    elif from_number == to_number:
        await message.answer(f"Число {from_number}")
    else:
        await message.answer(f"Число {random.randint(from_number, to_number)}")


@router.message(Tools_form.random_emoji)
async def send_random_emoji(message: Message):
    emoji = emoji_string[random.randint(0, len(emoji_string))]
    await message.text(f"Эмодзи <code>{emoji}</code>")


@router.message(
    StateFilter(Tools_form.random_input_value, Tools_form.random_emoji),
    F.text == "🔙 Назад",
)
async def return_to_main_menu(message: Message, state: FSMContext):
    await message.answer("Выберите инструмент", reply_markup=tools_kb)
    await state.set_state(Tools_form.start_menu)
