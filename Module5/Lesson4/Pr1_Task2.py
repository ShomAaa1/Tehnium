import csv
from collections import defaultdict
from datetime import datetime


def analyze_sales(filename: str) -> None:
    total_sales = 0
    product_count = defaultdict(int) # количество продаж продукта
    monthly_sales = defaultdict(int) # продажи по месяцам

    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            amount = int(row['Сумма'])
            product = row['Продукт']

            # общая сумма
            total_sales += amount

            # по количеству продаж (встречаемость)
            product_count[product] += 1

            # по месяцам
            date = datetime.strptime(row['Дата'], '%Y-%m-%d')
            month = date.strftime('%Y-%m') # только год-месяц
            monthly_sales[month] += amount

    # вывод
    print(f'Общая сумма продаж: {total_sales} руб.')

    # продукт с наибольшим количеством продаж
    top_product = max(product_count, key=product_count.get)
    print(f'Самый популярный продукт: {top_product} ({product_count[top_product]} раза)')

    print('Продажи по месяцам:')
    for month, total in monthly_sales.items():
        print(f'    {month}: {total} руб.')


if __name__ == '__main__':
    analyze_sales('sales.csv')