import sqlite3

DB_NAME = "library.db"


def create_db():
    """Создание базы и таблицы"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
    """)
    conn.commit()
    conn.close()


def add_book(title, author, year=None):
    """Добавление новой книги"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()


def get_all_books():
    """Получение списка всех книг"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


def update_book(book_id, title, author, year=None):
    """Обновление информации о книге"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books 
        SET title = ?, author = ?, year = ? 
        WHERE id = ?
    """, (title, author, year, book_id))
    conn.commit()
    conn.close()


def delete_book(book_id):
    """Удаление книги по id"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()


# === Тестовый код ===
if __name__ == "__main__":
    create_db()

    # Добавим книги
    add_book("Война и мир", "Лев Толстой", 1869)
    add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
    add_book("Мастер и Маргарита", "Михаил Булгаков")

    print("📚 Все книги после добавления:")
    for book in get_all_books():
        print(book)

    # Обновим книгу
    update_book(1, "Война и мир (обновлено)", "Л. Н. Толстой", 1873)

    print("\n📚 Все книги после обновления:")
    for book in get_all_books():
        print(book)

    # Удалим книгу
    delete_book(2)

    print("\n📚 Все книги после удаления:")
    for book in get_all_books():
        print(book)
