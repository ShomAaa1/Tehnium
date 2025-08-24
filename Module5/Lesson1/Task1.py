import string


def get_words(filename):
    with open(filename, 'r', encoding='utf8') as f:
        data = f.read()
        data = data.replace('\n', ' ')
        data_no_punct = ''.join(ch for ch in data if ch not in string.punctuation)
        words = data_no_punct.lower().split()
        return words


def get_words_dict(words):
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input('Введите название файла: ')
    our_words = get_words(filename)
    our_words_dict = get_words_dict(our_words)
    print('Кол-во слов: ', len(our_words))
    print('Кол-во уникальных слов: ', len(our_words_dict))
    print('Все использованные слова:')
    for word, count in sorted(our_words_dict.items()):
        print(word, count)


if __name__ == '__main__':
    main()