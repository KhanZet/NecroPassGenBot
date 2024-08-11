data = await state.get_data()
        option = int(data.get("selected_option"))
        value = int(message.text)

        users = jt.read_json(jt.user_settings_path)
        user = jt.find_user_by_id(users, message.from_user.id)
        user_found = False
        if not is_fixed:
            if (
                option == 1
                and value > user["password_settings"]["length"]["max_length"]
            ):
                await message.answer(
                    "Минимальная длина не может быть больше максимальной..."
                )
            elif (
                option == 2
                and value < user["password_settings"]["length"]["min_length"]
            ):
                await message.answer(
                    "Максимальная длина не может быть меньше минимальной..."
                )
            else:
                for user in users:
                    if user["user_id"] == message.from_user.id:
                        user_found = True
                        if is_fixed:
                            if option == 1:
                                user["password_settings"]["length"][
                                    "total_length"
                                ] = value
                        else:
                            if option == 1:
                                user["password_settings"]["length"][
                                    "min_length"
                                ] = value
                            elif option == 2:
                                user["password_settings"]["length"][
                                    "max_length"
                                ] = value

        if not user_found:
            await message.answer("Пользователь не найден")
        jt.write_json(users, jt.user_settings_path)
        await message.answer(get_settings_msg(message)[0])
        if is_fixed:
            await message.answer(
                f"В опцию {option} записанно значение {value}",
                reply_markup=configure_settings_kb_fixed_length,
            )
        else:
            await message.answer(
                f"В опцию {option} записанно значение {value}",
                reply_markup=configure_settings_kb,
            )
        await state.set_state(Settings_form.configure)
