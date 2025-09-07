from collections import defaultdict


# Создаем defaultdict, где значения по умолчанию будут списками
my_dict = defaultdict(list)

my_dict['фрукты'].append('яблоко')
my_dict['фрукты'].append('банан')
my_dict['фрукты'].append('груша')

my_dict['овощи'].append('морковь')
my_dict['овощи'].append('картофель')

my_dict['напитки'].append('чай')

# Выводим содержимое словаря
for key, values in my_dict.items():
    print(f'{key}: {values}')