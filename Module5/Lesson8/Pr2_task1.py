import random
from collections import Counter


def analyze_numbers(n: int = 30, min_val: int = 1, max_val: int = 10):
    # генерируем список случайных чисел
    numbers = [random.randint(min_val, max_val) for _ in range(n)]
    print('Сгенерированный список:', numbers)

    # считаем частоты
    counter = Counter(numbers)
    unique_count = len(counter) # количество уникальных элементов
    print('\nЧастоты:', counter)
    print('Количество уникальных элементов:', unique_count)

    # три самых частых элемента
    top_three = counter.most_common(3)
    print('\nТри наиболее часто встречающихся элемента:')
    for num, count in top_three:
        print(f'Элемент {num}: {count} раз(а)')


analyze_numbers()
