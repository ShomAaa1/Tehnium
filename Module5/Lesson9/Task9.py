import telebot
import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TG_TOKEN"))

DATA_FILE = "data.json"


def load_all_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_all_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)


def parse_time(dt_str):
    return datetime.fromisoformat(dt_str)


def get_last_record(user_id: str):
    """Безопасно вернуть последнюю запись сна пользователя"""
    user_data = all_data.get(user_id)
    if not user_data:
        return None
    history = user_data.get("history")
    if not history:
        return None
    return history[-1]


all_data = load_all_data()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я помогу отслеживать твой сон 🛌\n"
        "/sleep — перед сном\n"
        "/wake — после пробуждения\n"
        "/rate <оценка> — оценить сон (1–10)\n"
        "/note <текст> — добавить комментарий",
    )


@bot.message_handler(commands=["sleep"])
def go_to_sleep(message):
    user_id = str(message.from_user.id)
    now = datetime.now()

    sleep_record = {
        "start_time": now.isoformat(),
        "duration": None,
        "quality": None,
        "notes": "",
    }

    all_data.setdefault(user_id, {}).setdefault("history", []).append(sleep_record)
    save_all_data(all_data)

    bot.send_message(message.chat.id, f"Отметил, что ты лег спать в {now.strftime('%H:%M:%S')} 😴")


@bot.message_handler(commands=["wake"])
def wake_up(message):
    user_id = str(message.from_user.id)
    last_record = get_last_record(user_id)

    if not last_record:
        bot.send_message(message.chat.id, "Нет данных о сне. Используй /sleep перед сном.")
        return

    if last_record["duration"] is not None:
        bot.send_message(message.chat.id, "Ты уже отметил пробуждение.")
        return

    start_time = parse_time(last_record["start_time"])
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() / 3600

    last_record["duration"] = round(duration, 2)
    save_all_data(all_data)

    bot.send_message(message.chat.id, f"Ты спал {duration:.2f} часов. Доброе утро! 🌅")


@bot.message_handler(commands=["rate"])
def rate_sleep(message):
    user_id = str(message.from_user.id)
    last_record = get_last_record(user_id)

    if not last_record:
        bot.send_message(message.chat.id, "Нет данных о сне. Сначала используй /sleep.")
        return

    try:
        quality = int(message.text.split(maxsplit=1)[1])
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Укажи оценку сна числом от 1 до 10.\nПример: /rate 8")
        return

    if not 1 <= quality <= 10:
        bot.send_message(message.chat.id, "Оценка должна быть от 1 до 10.")
        return

    last_record["quality"] = quality
    save_all_data(all_data)

    bot.send_message(message.chat.id, f"Оценка сна сохранена: {quality}/10 🌙")


@bot.message_handler(commands=["note"])
def add_note(message):
    user_id = str(message.from_user.id)
    last_record = get_last_record(user_id)

    if not last_record:
        bot.send_message(message.chat.id, "Нет данных о сне. Сначала используй /sleep.")
        return

    try:
        note = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_message(message.chat.id, "Пожалуйста, добавь текст комментария.\nПример: /note Проснулся бодрым")
        return

    last_record["notes"] = note
    save_all_data(all_data)

    bot.send_message(message.chat.id, "Комментарий сохранен 📝")


bot.polling(none_stop=True)
