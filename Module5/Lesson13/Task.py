from functools import reduce

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 10, 15, 20]


# --- 1. map() и обычная функция ---
def cube(x):
    return x ** 3


cubes = list(map(cube, numbers))
print("Кубы чисел:", cubes)


# --- 2. filter() и обычная функция ---
def divisible_by_5(x):
    return x % 5 == 0


div_by_5 = list(filter(divisible_by_5, numbers))
print("Числа, делящиеся на 5:", div_by_5)


# --- 3. filter() + reduce() для произведения нечётных чисел ---
def is_odd(x):
    return x % 2 == 1


def multiply(x, y):
    return x * y


odd_numbers = list(filter(is_odd, numbers))
product_of_odds = reduce(multiply, odd_numbers, 1)

print("Нечётные числа:", odd_numbers)
print("Произведение нечётных чисел:", product_of_odds)
