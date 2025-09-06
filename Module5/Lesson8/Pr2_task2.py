from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'genre'])

book1 = Book(title='Преступление и наказание', author='Ф. М. Достоевский', genre='Роман')
book2 = Book(title='Война и мир', author='Л. Н. Толстой', genre='Эпопея')
book3 = Book(title='Мастер и Маргарита', author='М. А. Булгаков', genre='Фантастика')

for book in (book1, book2, book3):
    print(f'Название: {book.title}, Автор: {book.author}, Жанр: {book.genre}')