import csv

# with open('data.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# with open('data.csv') as f:
#     reader = csv.reader(f)
#     print(list(reader))

# data = [
#     ['Имя', 'Возраст', 'Город'],
#     ['Анна', '25', 'Москва'],
#     ['Петр', '30', 'Санкт-Петербург'],
#     ['Мария', '28', 'Киев']
# ]
#
# with open('новые_данные.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)

# data = [
#     {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
#     {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
#     {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
# ]
#
# with open('данные_с_заголовками.csv', 'w') as csvfile:
#     fieldnames = ['Имя', 'Возраст', 'Город']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerows(data)
#
# with open('данные_с_заголовками.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Имя'], row['Возраст'], row['Город'])
        # print(row)

# with open('данные_с_заголовками.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         print(row)


def txt_to_csv(txt_filename:str, csv_filename:str) -> None:
    with open(txt_filename, 'r', encoding='utf-8') as f_in, \
            open(csv_filename, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)

        for line in f_in:
            row = line.strip().split('\t')
            writer.writerow(row)


def calc_total(csv_filename: str) -> int:
    total = 0
    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            name, qty, price = row[0], int(row[1]), int(row[2])
            total += qty * price
    return total


def main():
    txt_file = 'prices.txt'
    csv_file = 'prices.csv'

    txt_to_csv(txt_file, csv_file)
    total_price = calc_total(csv_file)
    print('Общая стоимость заказа:', total_price, 'руб.')


if __name__ == "__main__":
    main()