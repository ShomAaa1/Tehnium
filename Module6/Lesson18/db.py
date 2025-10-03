import sqlite3
from datetime import datetime

DB_NAME = 'sleepbot.db'


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Таблица пользователей
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    # Таблица записей сна
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sleep_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        sleep_time DATETIME,
        wake_time DATETIME,
        sleep_quality INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Таблица заметок
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sleep_record_id INTEGER,
        text TEXT,
        FOREIGN KEY(sleep_record_id) REFERENCES sleep_records(id)
    )
    """)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_NAME)


def add_user(user_id: int, name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)', (user_id, name))
    conn.commit()
    conn.close()


def get_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cur.fetchone()
    conn.close()
    return user


def start_sleep(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO sleep_records (user_id, sleep_time) VALUES (?, ?)',
        (user_id, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def wake_up(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id, sleep_time FROM sleep_records WHERE user_id=? AND wake_time IS NULL ORDER BY id DESC LIMIT 1',
        (user_id,)
    )
    record = cur.fetchone()
    if not record:
        conn.close()
        return None

    record_id, sleep_time = record
    wake_time = datetime.now()
    cur.execute('UPDATE sleep_records SET wake_time=? WHERE id=?', (wake_time.isoformat(), record_id))
    conn.commit()
    conn.close()

    sleep_duration = (wake_time - datetime.fromisoformat(sleep_time)).total_seconds() / 3600
    return round(sleep_duration, 2)


def rate_sleep(user_id: int, quality: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id FROM sleep_records WHERE user_id=? AND wake_time IS NOT NULL AND sleep_quality IS NULL ORDER BY id DESC LIMIT 1',
        (user_id,)
    )
    record = cur.fetchone()
    if not record:
        conn.close()
        return False

    record_id = record[0]
    cur.execute('UPDATE sleep_records SET sleep_quality=? WHERE id=?', (quality, record_id))
    conn.commit()
    conn.close()
    return True


def add_note(user_id: int, text: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT id FROM sleep_records WHERE user_id=? ORDER BY id DESC LIMIT 1',
        (user_id,)
    )
    record = cur.fetchone()
    if not record:
        conn.close()
        return False
    record_id = record[0]
    cur.execute('INSERT INTO notes (sleep_record_id, text) VALUES (?, ?)', (record_id, text))
    conn.commit()
    conn.close()
    return True


def get_sleep_history(user_id: int, limit: int = 5):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT sleep_time, wake_time, sleep_quality
        FROM sleep_records
        WHERE user_id=?
        ORDER BY sleep_time DESC
        LIMIT ?
    """, (user_id, limit))
    rows = cur.fetchall()
    conn.close()
    return rows
