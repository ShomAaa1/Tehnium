import datetime
import calendar

import now

now = datetime.datetime.now()
print(f'Текущая дата и время: {now}')

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
print(f'Сегодня: {days[now.weekday()]}')

year = now.year
if calendar.isleap(year):
    print(f'Год {year} - високосный.')
else:
    print(f'Год {year} - не високосный.')

user_input = input('\nВведите любую дату в формате ГГГГ-ММ-ДД: ')
try:
    user_date = datetime.datetime.strptime(user_input, '%Y-%m-%d')
except ValueError:
    print('Ошибка: неверный формат даты! Нужно ГГГГ-ММ-ДД.')
    exit()

delta = abs(user_date - now)
print(f'Между {now.date()} и {user_input} прошло {delta.days} дней.')
days_diff = delta.days
hours_diff, remainder = divmod(delta.seconds, 3600)
minutes_diff, _ = divmod(remainder, 60)

print(f'Разница: {days_diff} дней, {hours_diff} часов, {minutes_diff} минут.')