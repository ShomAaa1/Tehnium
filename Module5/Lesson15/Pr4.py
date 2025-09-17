# Task 1
students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}

# Сортировка по возрасту
sorted_students = sorted(students_dict.items(), key=lambda item: item[1])

print(sorted_students)

# Task 2
data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]


# Функция для вычисления BMI
def bmi(person):
    weight, height_cm = person
    height_m = height_cm / 100
    return weight / (height_m ** 2)


# Сортировка по BMI
sorted_data = sorted(data, key=bmi)

print("Отсортировано по BMI:")
for w, h in sorted_data:
    print(f"Вес: {w} кг, Рост: {h} см, BMI: {bmi((w, h)):.2f}")

# Task 3
students_list = [
    {"name": "Саша", "age": 27},
    {"name": "Кирилл", "age": 52},
    {"name": "Маша", "age": 14},
    {"name": "Петя", "age": 36},
    {"name": "Оля", "age": 43},
]

# Ищем минимальный возраст
youngest_student = min(students_list, key=lambda s: s["age"])

print("Самый младший ученик:", youngest_student)
