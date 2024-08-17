from aiogram.fsm.state import StatesGroup, State


class Settings_form(StatesGroup):
    settings = State()
    configure = State()
    select_option = State()
    input_value = State()
    toggle_option = State()


class Account_form(StatesGroup):
    start_menu = State()


class Market_form(StatesGroup):
    pass


class Password_gen_form(StatesGroup):
    pass


class Help_form(StatesGroup):
    pass


class Tools_form(StatesGroup):
    start_menu = State()
    random_input_value = State()
    random_emoji = State()
    random_swear = State()
