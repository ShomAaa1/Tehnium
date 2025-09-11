import csv
from collections import defaultdict
from datetime import datetime


def analyze_sales(filename: str) -> None:
    total_sales = 0
    product_sales = defaultdict(int) # сумма продаж по продукту
    monthly_sales = defaultdict(int) # продажи по месяцам

    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            amount = int(row['Сумма'])
            product = row['Продукт']

            # общая сумма
            total_sales += amount

            # суммарные продажи по продуктам
            product_sales[product] += amount

            # по месяцам
            date = datetime.strptime(row['Дата'], '%Y-%m-%d')
            month = date.strftime('%Y-%m') # только год-месяц
            monthly_sales[month] += amount

    # вывод
    print(f'Общая сумма продаж: {total_sales} руб.')

    # продукт с наибольшим объемом продаж
    top_product = max(product_sales, key=product_sales.get)
    print(f'Продукт с наибольшим объемом продаж: {top_product} ({product_sales[top_product]} руб.)')

    print('Продажи по месяцам:')
    for month, total in monthly_sales.items():
        print(f'    {month}: {total} руб.')


if __name__ == '__main__':
    analyze_sales('sales.csv')