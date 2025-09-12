from itertools import combinations
from itertools import permutations
import itertools


numbers = [1, 2, 3, 4]

# создаем все комбинации длиной 2
comb = combinations(numbers, 2)

for c in comb:
    print(c)


word = 'Python'
# создаем все перестановки букв
perms = permutations(word)

for p in perms:
    print(''.join(p))


list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']

# Берем ровно 5 * len(combined) элементов из бесконечного цикла
result = list(itertools.islice(itertools.cycle(itertools.chain(list1, list2, list3)), 5 * (len(list1) + len(list2) + len(list3))))

print(result)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# первые 10 чисел
fib10 = list(itertools.islice(fibonacci(), 10))
print(fib10)


colors = ['red', 'blue']
items = ['shirt', 'shoes']

for combo in itertools.product(colors, items):
    print(' '.join(combo))
