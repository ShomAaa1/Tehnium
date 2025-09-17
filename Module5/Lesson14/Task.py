# 1. filter() + lambda для строк длиннее 4 символов
words = ["apple", "kiwi", "banana", "fig"]
filtered_words = list(filter(lambda x: len(x) > 4, words))
print("Строки длиннее 4 символов:", filtered_words)


# 2. max() + lambda для поиска студента с максимальной оценкой
students = [
    {"name": "John", "grade": 90},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 92}
]
best_student = max(students, key=lambda s: s["grade"])
print("Лучший студент:", best_student)


# 3. sorted() + lambda для сортировки по сумме элементов кортежей
tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_tuples = sorted(tuples, key=lambda x: x[0] + x[1])
print("Отсортированные кортежи:", sorted_tuples)


# 4. filter() + lambda для чётных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Чётные числа:", even_numbers)


# 5. sorted() + lambda для объектов класса
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # для красивого вывода
        return f"{self.name} ({self.age})"


people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

sorted_people = sorted(people, key=lambda p: p.age)
print("Отсортированные люди по возрасту:", sorted_people)
