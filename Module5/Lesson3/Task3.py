import json


def csv_to_json(
        csv_filename: str,
        json_filename: str,
        delimiter: str = ',',
        line_sep: str = '\n'
) -> None:
    """
    Конвертер CSV-файла в JSON-файл.
    :param csv_filename: путь к входному CSV-файлу
    :param json_filename: путь к выходному JSON-файлу
    :param delimiter: символ-разделитель между значениями в CSV
    :param line_sep: символ-разделитель строк
    :return: None
    """
    with open(csv_filename, 'r', encoding='utf-8') as f:
        csv_text = f.read()

    # Убираем пробелы по краям и разбиваем на строки
    lines = csv_text.strip().split(line_sep)
    if not lines:
        with open(json_filename, 'w', encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        return

    # Заголовки
    headers = [h.strip() for h in lines[0].split(delimiter)]

    rows = []
    for line in lines[1:]:
        if not line.strip(): # пропускаем пустые строки
            continue
        values = line.split(delimiter)
        row = {}
        for col, val in zip(headers, values):
            val = val.strip()
            if val.isdigit():
                row[col] = int(val)
            else:
                row[col] = val
        rows.append(row)

    # Записываем результат в JSON-файл
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=4, ensure_ascii=False)


def main():
    csv_filename = 'prices_2.csv'
    json_filename = 'prices.json'
    csv_to_json(csv_filename, json_filename)


if __name__ == '__main__':
    main()
