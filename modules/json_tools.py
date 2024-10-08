import json
from pathlib import Path
import datetime as dt


def find_user_by_id(users, id):
    for user in users:
        if user["user_id"] == id:
            return user
    return None


def read_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def add_user(user_data, file_path):
    users = read_json(file_path)
    users.append(user_data)
    write_json(users, file_path)


def add_password(user, date, password):
    print(user)
    if "history" not in user:
        user["history"] = {}
    if date in user["history"]:
        user["history"][date].append(password)
    else:
        user["history"][date] = [password]


def create_user(user_id, username):
    user_data = {"user_id": user_id, "username": username, "history": {}}
    user_settings = {
        "user_id": user_id,
        "password_settings": {
            "length": {
                "min_length": 8,
                "max_length": 16,
                "total_length": 15,
                "fixed_length": True,
            },
            "include_uppercase": True,
            "include_lowercase": True,
            "include_digits": True,
            "include_specials": True,
        },
    }

    if find_user_by_id(read_json(user_settings_path), user_id):
        print("Данные пользователя есть в базе")
    else:
        add_user(user_data, user_data_path)

    if find_user_by_id(read_json(user_settings_path), user_id):
        print("Настройки пользователя есть в базе")
    else:
        add_user(user_settings, user_settings_path)


user_data_path = Path(__file__).parent.parent / "data" / "user_data.json"
user_settings_path = Path(__file__).parent.parent / "data" / "user_settings.json"
