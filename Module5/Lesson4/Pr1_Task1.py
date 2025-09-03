import json


def analyze_students(filename: str, subject: str) -> None:
    with open(filename, 'r', encoding='utf-8') as f:
        students = json.load(f)
    # общее количество студентов
    total = len(students)
    print(f'Всего студентов: {total}')

    oldest = max(students, key=lambda s: s['возраст'])
    print(f'Самый старший студент: {oldest["имя"]}, {oldest["возраст"]} лет, город {oldest["город"]}')

    subject_count = sum(1 for s in students if subject in s['предметы'])
    print(f'Студентов, изучающих {subject}: {subject_count}')


if __name__ == '__main__':
    analyze_students('students.json', 'Python')