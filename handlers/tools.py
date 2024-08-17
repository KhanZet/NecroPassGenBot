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
polish_swears = {
    "kurwa": "блядь",
    "pierdolić": "ебать",
    "chuj": "хуй",
    "skurwiel": "сукин сын",
    "dziwka": "шлюха",
    "pizda": "пизда",
    "jebany": "ёбаный",
    "spierdalaj": "иди нахуй",
    "zjebać": "наебать",
    "kurwa mać": "блядь мать",
    "chuj ci w dupę": "хуй тебе в жопу",
    "gówno": "дерьмо",
    "kutas": "хуй",
    "jebac": "ебать",
    "spierdolić": "съебаться",
    "zajebisty": "охуенный",
    "cholera": "черт",
    "skurwysyn": "сукин сын",
    "dupek": "мудак",
    "pieprzyć": "ебать",
    "pierdolenie": "ебля",
    "suka": "сука",
    "jebaka": "ебарь",
    "jebany skurwysyn": "ёбаный сукин сын",
    "pieprzony": "ёбаный",
    "jebane": "ёбаное",
    "pierdolony": "ёбаный",
    "gówniany": "дерьмовый",
    "kurewski": "сукин",
    "sukinsyn": "сукин сын",
    "zjebany": "наебанный",
    "chujowo": "хреново",
    "gówniarz": "говнюк",
    "popierdolony": "ёбнутый",
    "jebany dupek": "ёбаный мудак",
    "skurwiony": "засранный",
    "pierdolić się": "ебаться",
    "cholerny": "чёртов",
    "skurwiony chuj": "засранный хуй",
    "pierdolenie": "ёбань",
    "chujek": "хуйчишка",
    "dupa": "жопа",
    "jebaniec": "ёбантяй",
    "jebane gówno": "ёбаное дерьмо",
    "pieprzony kutas": "ёбаный хуй",
    "pierdolić to": "нахуй это",
    "skurwysyn jebany": "сукин сын ёбаный",
    "kurwa jebana": "блядь ёбаная",
    "pizda jebana": "пизда ёбаная",
    "skurwysyn pierdolony": "сукин сын ёбаный",
    "gówniany kutas": "дерьмовый хуй",
    "pierdol się": "иди нахуй",
    "chuj ci w mordę": "хуй тебе в морду",
    "kurwa twoja mać": "блядь твоя мать",
    "skurwysyński": "сукин",
    "skurwieniec": "засранец",
    "skurwysyn chuj": "сукин сын хуй",
    "kurwiarz": "блядун",
    "jebaka skurwiel": "ебарь сукин сын",
    "pierdolic skurwysyna": "ебать сукина сына",
    "gówniarz pierdolony": "говнюк ёбаный",
    "kurwa pierdolona": "блядь ёбаная",
    "pierdolić w dupę": "ебать в жопу",
    "skurwysyn jebany w dupę": "сукин сын ёбаный в жопу",
    "jebana dziwka": "ёбаная шлюха",
    "pierdolić kurwę": "ебать блядь",
    "chuj w dupę": "хуй в жопу",
    "pierdolić kurwy": "ебать шлюх",
    "kurwa dziwka": "блядь шлюха",
    "pierdolić skurwysyna": "ебать сукина сына",
    "jebane dziwki": "ёбаные шлюхи",
    "skurwiony kurwiarz": "засранный блядун",
    "pierdolić kurwę w dupę": "ебать блядь в жопу",
    "chujowa kurwa": "хреновая блядь",
    "jebana suka": "ёбаная сука",
    "skurwysyństwo": "сукины дела",
    "pierdolić życie": "ебать жизнь",
    "chujowy dzień": "хреновый день",
    "jebana praca": "ёбаная работа",
    "gówniane życie": "дерьмовая жизнь",
    "kurwa jego mać": "блядь его мать",
    "pierdolić szkołę": "ебать школу",
    "chujowa pogoda": "хреновая погода",
    "jebana robota": "ёбаная работа",
    "kurwa chuj": "блядь хуй",
    "pierdolić to wszystko": "нахуй всё это",
    "jebany świat": "ёбаный мир",
    "kurwa jego mać jebana": "блядь его мать ёбаная",
    "gówno do dupy": "дерьмо в жопу",
    "pierdolić wszystko": "нахуй всё",
    "skurwysyn jebany kurwa": "сукин сын ёбаная блядь",
    "jebana pogoda": "ёбаная погода",
    "kurwa gówno": "блядь дерьмо",
    "pierdolić wszystkich": "ебать всех",
}


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
    elif message.text == "Случайный польский мат":
        polish_swear = random.choice(list(polish_swears.items()))
        await message.answer(
            f"<b><i>Польский мат</i></b>  <code>{polish_swear[0]}</code>\n<b>Означает</b> {polish_swear[1]}"
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


@router.message(
    StateFilter(Tools_form.random_input_value, Tools_form.random_emoji),
    F.text == "🔙 Назад",
)
async def return_to_main_menu(message: Message, state: FSMContext):
    await message.answer("Выберите инструмент", reply_markup=tools_kb)
    await state.set_state(Tools_form.start_menu)
