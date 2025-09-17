import json
import pprint
import csv

# Чтение JSON
with open('student_list.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

# Проверяем
print(type(students))  # <class 'dict'>
print(students.keys()) # Все имена студентов
print(students)


# Task2
def get_average_scores(students_dict):
    """Возвращает словарь: имя студента -> средний балл"""
    averages = {}
    for name, info in students_dict.items():
        grades = info.get("grades", {})
        if grades:
            averages[name] = sum(grades.values()) / len(grades)
    return averages


# Пример использования:
print(get_average_scores(students))


def get_best_student(students_dict):
    averages = get_average_scores(students_dict)
    best_name = max(averages, key=averages.get)
    print(f"Наилучший студент: {best_name} (Средний балл: {averages[best_name]:.2f})")


def get_worst_student(students_dict):
    averages = get_average_scores(students_dict)
    worst_name = min(averages, key=averages.get)
    print(f"Худший студент: {worst_name} (Средний балл: {averages[worst_name]:.2f})")


# Пример использования:
get_best_student(students)
get_worst_student(students)


# Task 3
def find_student(name: str):
    student = students.get(name)
    if student:
        print(f"Имя: {name}")
        print(f"Возраст: {student.get('age')}")
        print(f"Предметы: {student.get('subjects')}")
        print(f"Оценки: {student.get('grades')}")
    else:
        print("Студент с таким именем не найден")


# Примеры использования:
find_student("John")
find_student("Emma")


# Task 4
def sort_students_by_average(students_dict: dict):
    # Сначала создаем список кортежей (имя, средний балл)
    averages = []
    for name, info in students_dict.items():
        grades = info.get("grades", {})
        if grades:
            avg = sum(grades.values()) / len(grades)
            averages.append((name, avg))

    # Сортируем по среднему баллу в порядке убывания
    sorted_students = sorted(averages, key=lambda x: x[1], reverse=True)

    # Выводим результат
    print("Сортировка студентов по среднему баллу:")
    for name, avg in sorted_students:
        print(f"{name}: {avg:.2f}")


# Пример использования:
sort_students_by_average(students)


# Task 5
# Преобразование словаря в список словарей
students_list = [
    {
        'name': name,
        'age': info.get('age'),
        'subjects': info.get('subjects', []),
        'grades': info.get('grades', {})
    }
    for name, info in students.items()
]

# Проверка
# for student in students_list:
#     print(student)
pprint.pprint(students_list)


# Task 6
# Загружаем студентов из JSON
with open('student_list.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

# Создаем CSV файл
with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Записываем заголовки
    writer.writerow(['name', 'age', 'grade'])

    for name, info in students.items():
        grades = info.get('grades', {})
        if grades:
            average = sum(grades.values()) / len(grades)
        else:
            average = 0
        # Записываем строку с данными
        writer.writerow([name, info.get('age', ''), round(average, 2)])

print("CSV файл сформирован: students.csv")