import os


main_dir = 'Управление_файлами'
os.makedirs(main_dir, exist_ok=True)

file1 = os.path.join(main_dir, 'file1.txt')
file2 = os.path.join(main_dir, 'file2.txt')

with open(file1, 'w', encoding='utf-8') as f:
    f.write('Это содержимое первого файла.\n')
with open(file2, 'w', encoding='utf-8') as f:
    f.write('Это содержимое второго файла.\n')

print('Содержимое директории после создания файлов:')
print(os.listdir(main_dir))

os.remove(file1)

sub_dir = os.path.join(main_dir, 'Поддиректория')
os.makedirs(sub_dir, exist_ok=True)

new_path = os.path.join(sub_dir, 'file2.txt')
os.rename(file2, new_path)


def remove_dir_recursive(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            p = os.path.join(root, name)
            try:
                os.remove(p)
            except Exception as e:
                print(f'Не удалось удалить файл: {p}.')
        for name in dirs:
            p = os.path.join(root, name)
            try:
                if os.path.islink(p):
                    os.unlink(p)
                else:
                    os.rmdir(p)
            except Exception as e:
                print(f'Не удалось удалить каталог: {p}.')
    try:
        os.rmdir(path)
    except Exception as e:
        print(f'Не удалось удалить корневую директорию: {path}.')

remove_dir_recursive(main_dir)