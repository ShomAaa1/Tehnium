import itertools


def generate_deck():
    """Создает стандартную колоду из 52 карт"""
    suits = ['♠', '♥', '♦', '♣']  # пики, черви, бубны, трефы
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'J', 'Q', 'K', 'A']
    return [rank + suit for suit in suits for rank in ranks]


def generate_combinations(deck, k, save_to_file=False):
    """Генерация всех комбинаций из k карт"""
    combos = itertools.combinations(deck, k)

    if save_to_file:
        filename = f"combinations_{k}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for combo in combos:
                f.write(", ".join(combo) + "\n")
        print(f"✅ Все комбинации сохранены в {filename}")
    else:
        for combo in combos:
            print(combo)


if __name__ == "__main__":
    deck = generate_deck()
    print("Стандартная колода:", deck)

    k = int(input("Введите количество карт для комбинации (от 1 до 52): "))

    if 1 <= k <= 52:
        generate_combinations(deck, k, save_to_file=True)
    else:
        print("Ошибка: число должно быть от 1 до 52.")
