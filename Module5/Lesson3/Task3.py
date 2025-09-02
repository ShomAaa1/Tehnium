import csv
import json

def csv_to_json(csv_filename: str, delimiter: str = ',', lineterminator: str = '\n') -> str:
    """
    Преобразует CSV в JSON строку
    :param csv_filename: путь к CSV файлу
    :param delimiter: разделитель значений (по умолчанию ',')
    :param lineterminator: разделитель строк (по умолчанию '\n')
    :return: JSON строка с отступами = 4
    """
    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimiter, fieldnames=['товар', 'количество', 'цена'], lineterminator=lineterminator)
        data = list(reader) # [{col: val}, {col: val}, ...]

    # преобразуем список словарей в JSON строку
    return json.dumps(data, indent=4, ensure_ascii=False)


def main():
    csv_filename = 'prices.csv'
    json_str = csv_to_json(csv_filename)

    print(json_str)


if __name__ == '__main__':
    main()
