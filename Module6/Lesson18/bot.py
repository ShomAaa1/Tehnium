import telebot
import os
from datetime import datetime
from dotenv import load_dotenv
from db import init_db, add_user, start_sleep, wake_up, rate_sleep, add_note, get_sleep_history

load_dotenv()
bot = telebot.TeleBot(os.getenv("TG_TOKEN"))

# инициализация БД
init_db()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    add_user(message.from_user.id, message.from_user.first_name)
    bot.send_message(
        message.chat.id,
        "Привет! Я помогу отслеживать твой сон 🛌\n"
        "/sleep — перед сном\n"
        "/wake — после пробуждения\n"
        "/rate <оценка> — оценить сон (1–10)\n"
        "/note <текст> — добавить комментарий"
        "/history - история записей",
    )


@bot.message_handler(commands=["sleep"])
def go_to_sleep(message):
    user_id = message.from_user.id
    start_sleep(user_id)
    now = datetime.now()
    bot.send_message(message.chat.id, f"Отметил, что ты лег спать в {now.strftime('%H:%M:%S')} 😴")


@bot.message_handler(commands=["wake"])
def wake_up_handler(message):
    user_id = message.from_user.id
    duration = wake_up(user_id)
    if duration is None:
        bot.send_message(message.chat.id, "Нет данных о сне. Используй /sleep перед сном.")
    else:
        bot.send_message(message.chat.id, f"Ты спал {duration:.2f} часов. Доброе утро! 🌅")


@bot.message_handler(commands=["rate"])
def rate_sleep_handler(message):
    user_id = message.from_user.id
    try:
        quality = int(message.text.split(maxsplit=1)[1])
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Укажи оценку сна числом от 1 до 10.\nПример: /rate 8")
        return

    if not 1 <= quality <= 10:
        bot.send_message(message.chat.id, "Оценка должна быть от 1 до 10.")
        return

    if rate_sleep(user_id, quality):
        bot.send_message(message.chat.id, f"Оценка сна сохранена: {quality}/10 🌙")
    else:
        bot.send_message(message.chat.id, "Нет завершённых записей сна для оценки.")


@bot.message_handler(commands=["note"])
def add_note_handler(message):
    user_id = message.from_user.id
    try:
        note = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_message(message.chat.id, "Пожалуйста, добавь текст комментария.\nПример: /note Проснулся бодрым")
        return

    if add_note(user_id, note):
        bot.send_message(message.chat.id, "Комментарий сохранен 📝")
    else:
        bot.send_message(message.chat.id, "Нет записей сна, к которым можно добавить комментарий.")


@bot.message_handler(commands=["history"])
def history_handler(message):
    user_id = message.from_user.id
    history = get_sleep_history(user_id, limit=5)

    if not history:
        bot.send_message(message.chat.id, "История сна пуста 💤")
        return

    reply = "📖 Последние записи сна:\n\n"
    for i, (sleep_time, wake_time, quality) in enumerate(history, 1):
        sleep_str = datetime.fromisoformat(sleep_time).strftime("%d.%m %H:%M")
        wake_str = datetime.fromisoformat(wake_time).strftime("%d.%m %H:%M") if wake_time else "—"
        q = quality if quality else "?"
        reply += f"{i}. Сон: {sleep_str} → {wake_str}, оценка: {q}/10\n"

    bot.send_message(message.chat.id, reply)


bot.polling(none_stop=True)
