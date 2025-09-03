import json
import csv


def analyze_employees(json_filename: str, csv_filename: str) -> None:
    with open(json_filename, 'r', encoding='utf-8') as f_json:
        employees = json.load(f_json)

    performance = {}
    with open(csv_filename, 'r', encoding='utf-8') as f_csv:
        reader = csv.DictReader(f_csv, delimiter=',')
        for row in reader:
            performance[int(row['employee_id'])] = int(row['performance'])

    # соединяем данные
    for emp in employees:
        emp_id = emp['id']
        emp['performance'] = performance.get(emp_id, None)

    # средняя производительность
    scores = [emp['performance'] for emp in employees if emp['performance'] is not None]
    avg_score = sum(scores) / len(scores)

    # лучший сотрудник
    best = max(employees, key=lambda e: e['performance'])

    # вывод
    print(f'Средняя производительность: {avg_score:.2f}')
    print(f'Лучший сотрудник: {best["имя"]} (производительность {best["performance"]})')


if __name__ == '__main__':
    analyze_employees('employees.json', 'performance.csv')
