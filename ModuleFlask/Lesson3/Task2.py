import requests


def get_latest_launch():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else: print('Ошибка при запросе:', resp.status_code)
        return None
    except requests.exceptions.ConnectionError:
        print('Ошибка: нет подключения к интернету.')
    except requests.exceptions.Timeout:
        print('Ошибка: запрос занял слишком много времени.')
    return None


data = get_latest_launch()
if data:
    name = data.get('name')
    date = data.get('date_utc')
    success = data.get('success')
    details = data.get('details')
    cores = data.get('cores', [])
    print(f'Запуск: {name}')
    print(f'Дата (UTC): {date}')
    print('Успех?' , 'Да' if success else 'Нет')
    if details:
        print('Подробнее:', details)
    print('Состав миссии:')
    for core in cores:
        print(' core id:', core.get('core'), 'полет:', core.get('flight'), 'успешное приземление:', core.get('landing_success'))
