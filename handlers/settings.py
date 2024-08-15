from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Settings_form
from keyboards.builders import any_kb
from keyboards.reply import (
    rmk,
    configure_settings_kb,
    configure_settings_kb_fixed_length,
    main,
)

from modules import json_tools as jt

router = Router()


def bool_to_str(value):
    return "✅ Вкл" if value else "❌ Выкл"


def get_settings_msg(message):
    users = jt.read_json(jt.user_settings_path)
    user = jt.find_user_by_id(users, message.from_user.id)
    if user == None:
        jt.create_user(message.from_user.id, message.from_user.username)
        users = jt.read_json(jt.user_settings_path)
        user = jt.find_user_by_id(users, message.from_user.id)

    fixed_length = user["password_settings"]["length"]["fixed_length"]

    if not fixed_length:
        settings_msg = (
            f"🆔 Идентификатор пользователя: {user['user_id']} \n\n"
            f"⭕️ Длина пароля:\n\n"
            f"💠 1.Минимальная длина: {user['password_settings']['length']['min_length']} 📏\n"
            f"💠 2.Максимальная длина: {user['password_settings']['length']['max_length']} 📏\n"
            f"💠 3.Фиксированная длина: {bool_to_str(user['password_settings']['length']['fixed_length'])} \n\n"
            f"⭕️ Настройка символов:\n\n"
            f"💠 4.Заглавные буквы: {bool_to_str(user['password_settings']['include_uppercase'])} \n"
            f"💠 5.Строчные буквы: {bool_to_str(user['password_settings']['include_lowercase'])} \n"
            f"💠 6.Цифры: {bool_to_str(user['password_settings']['include_digits'])} \n"
            f"💠 7.Специальные символы: {bool_to_str(user['password_settings']['include_specials'])} \n"
        )
    else:
        settings_msg = (
            f"🆔 Идентификатор пользователя: {user['user_id']} \n\n"
            f"⭕️ Длина пароля:\n\n"
            f"💠 1.Длина пароля: {user['password_settings']['length']['total_length']} 📏\n"
            f"💠 2.Фиксированная длина: {bool_to_str(user['password_settings']['length']['fixed_length'])} \n\n"
            f"⭕️ Настройка символов:\n\n"
            f"💠 3.Заглавные буквы: {bool_to_str(user['password_settings']['include_uppercase'])} \n"
            f"💠 4.Строчные буквы: {bool_to_str(user['password_settings']['include_lowercase'])} \n"
            f"💠 5.Цифры: {bool_to_str(user['password_settings']['include_digits'])} \n"
            f"💠 6.Специальные символы: {bool_to_str(user['password_settings']['include_specials'])} \n"
        )

    return settings_msg, fixed_length


@router.message((F.text == "⚙️ Настройки") | (F.text == "/settings"))
async def settings(message: Message, state: FSMContext):
    await message.answer(
        get_settings_msg(message)[0], reply_markup=any_kb(["🔙 Назад", "🔧 Настроить"])
    )
    await state.set_state(Settings_form.settings)


@router.message(Settings_form.settings, F.text == "🔙 Назад")
async def back_to_menu(message: Message, state: FSMContext):
    await message.answer("Вы вернулись в главное меню", reply_markup=main)
    await state.clear()


@router.message(Settings_form.settings, F.text == "🔧 Настроить")
async def configure_settings(message: Message, state: FSMContext):
    is_fixed = get_settings_msg(message)[1]
    if is_fixed:
        await message.answer(
            "Выберите опцию для настройки",
            reply_markup=configure_settings_kb_fixed_length,
        )
    else:
        await message.answer(
            "Выберите опцию для настройки", reply_markup=configure_settings_kb
        )
    await state.set_state(Settings_form.configure)


@router.message(Settings_form.configure)
async def select_option(message: Message, state: FSMContext):
    is_fixed = get_settings_msg(message)[1]
    if message.text == "🔙 Назад":
        await message.answer("Вы вернулись к настройкам")
        await message.answer(
            get_settings_msg(message)[0],
            reply_markup=any_kb(["🔙 Назад", "🔧 Настроить"]),
        )
        await state.set_state(Settings_form.settings)
    elif message.text.isdigit() and 1 <= int(message.text) <= 7:
        option = int(message.text)
        await state.update_data(selected_option=option)
        print(option)
        if (is_fixed and option == 1) or (not is_fixed and option in [1, 2]):
            await message.answer("Введите значение", reply_markup=any_kb(["🔙 Назад"]))
            await state.set_state(Settings_form.input_value)
        else:
            await message.answer(
                "✅   Включить    или    ❌   Выключить?",
                reply_markup=any_kb(["✅ Вкл", "❌ Выкл", "🔙 Назад"]),
            )
            await state.set_state(Settings_form.toggle_option)


@router.message(Settings_form.input_value)
async def input_value(message: Message, state: FSMContext):
    is_fixed = get_settings_msg(message)[1]
    if message.text == "🔙 Назад":
        if is_fixed:
            await message.answer(
                "Вы вернулись к выбору опций.",
                reply_markup=configure_settings_kb_fixed_length,
            )
        else:
            await message.answer(
                "Вы вернулись к выбору опций.", reply_markup=configure_settings_kb
            )

        await message.answer(get_settings_msg(message)[0])
        await state.set_state(Settings_form.configure)
    else:
        try:
            value = int(message.text)
        except ValueError:
            await message.answer("Пожалуйста введите числовое значение")
            return

        data = await state.get_data()
        option = int(data.get("selected_option"))
        users = jt.read_json(jt.user_settings_path)
        user = jt.find_user_by_id(users, message.from_user.id)
        if not user:
            await message.answer("Пользователь не найден")
            return
        if not is_fixed:
            min_length = user["password_settings"]["length"]["min_length"]
            max_length = user["password_settings"]["length"]["max_length"]

            if option == 1 and value > max_length:
                await message.answer(
                    f"Минимальная длина не может быть больше максимальной ({max_length})"
                )
                return
            elif option == 2 and value < min_length:
                await message.answer(
                    f"Максимальная длина не может быть меньше минимальной ({min_length})"
                )
                return
        if is_fixed:
            if option == 1:
                user["password_settings"]["length"]["total_length"] = value
        else:
            if option == 1:
                user["password_settings"]["length"]["min_length"] = value
            elif option == 2:
                user["password_settings"]["length"]["max_length"] = value

        print(users)

        jt.write_json(users, jt.user_settings_path)
        await message.answer(get_settings_msg(message)[0])
        if is_fixed:
            await message.answer(
                f"В опцию {option} записано значение {value}",
                reply_markup=configure_settings_kb_fixed_length,
            )
        else:
            await message.answer(
                f"В опцию {option} записано значение {value}",
                reply_markup=configure_settings_kb,
            )
        await state.set_state(Settings_form.configure)


@router.message(Settings_form.toggle_option)
async def toggle_option(message: Message, state: FSMContext):
    print(message.text)
    is_fixed = get_settings_msg(message)[1]
    if message.text == "🔙 Назад":
        if is_fixed:
            await message.answer(
                "Вы вернулись к выбору опций.",
                reply_markup=configure_settings_kb_fixed_length,
            )
        else:
            await message.answer(
                "Вы вернулись к выбору опций.", reply_markup=configure_settings_kb
            )
        await message.answer(get_settings_msg(message)[0])
        await state.set_state(Settings_form.configure)
    else:
        data = await state.get_data()
        option = data.get("selected_option")
        value = message.text
        if value == "✅ Вкл":
            value = True
        elif value == "❌ Выкл":
            value = False

        users = jt.read_json(jt.user_settings_path)
        user_found = False
        for user in users:
            if user["user_id"] == message.from_user.id:
                user_found = True
                if is_fixed:
                    if option == 2:
                        user["password_settings"]["length"]["fixed_length"] = value
                    elif option == 3:
                        user["password_settings"]["include_uppercase"] = value
                    elif option == 4:
                        user["password_settings"]["include_lowercase"] = value
                    elif option == 5:
                        user["password_settings"]["include_digits"] = value
                    elif option == 6:
                        user["password_settings"]["include_specials"] = value
                else:
                    if option == 3:
                        user["password_settings"]["length"]["fixed_length"] = value
                    elif option == 4:
                        user["password_settings"]["include_uppercase"] = value
                    elif option == 5:
                        user["password_settings"]["include_lowercase"] = value
                    elif option == 6:
                        user["password_settings"]["include_digits"] = value
                    elif option == 7:
                        user["password_settings"]["include_specials"] = value

        if not user_found:
            await message.answer("Пользователь не найден")

        jt.write_json(users, jt.user_settings_path)
        await message.answer(get_settings_msg(message)[0])
        status = False
        if value == True:
            status = "✅ Включена"
        else:
            status = "❌ Выключена"
        is_fixed = get_settings_msg(message)[1]
        if is_fixed:
            option = 2 if option == 3 else option
            await message.answer(
                f"Опция под номером {option} {status}",
                reply_markup=configure_settings_kb_fixed_length,
            )
        else:
            option = 3 if option == 2 else option
            await message.answer(
                f"Опция под номером {option} {status}",
                reply_markup=configure_settings_kb,
            )
        await state.set_state(Settings_form.configure)
