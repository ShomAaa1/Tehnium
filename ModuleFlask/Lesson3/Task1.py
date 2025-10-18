import requests
from collections import Counter


def get_repos(username):
    """
    Получает список публичных репозиториев пользователя GitHub.
    Возвращает список репозиториев или None в случае ошибки.
    """
    url = f'https://api.github.com/users/{username}/repos'
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print('Ошибка: такого пользователя не существует.')
            return None
        elif response.status_code == 403:
            print('Ошибка: превышен лимит запросов GitHub API.')
            return None
        elif response.status_code != 200:
            print(f'Неожиданная ошибка. Код состояния: {response.status_code}')
            return None

        return response.json()

    except requests.exceptions.ConnectionError:
        print('Ошибка: нет подключения к интернету.')
    except requests.exceptions.Timeout:
        print('Ошибка: запрос занял слишком много времени.')

    return None


def analyze_repos(repos):
    """
    Анализирует список репозиториев и выводит статистику:
    - количество репозиториев
    - суммарное число звезд
    - топовый репозиторий
    - используемые языки
    """
    if not repos:
        print('Нет данных для анализа.')
        return

    total_repos = len(repos)
    total_stars = sum(repo['stargazers_count'] for repo in repos)

    top_repo = max(repos, key=lambda repo: repo['stargazers_count'])
    top_repo_name = top_repo['name']
    top_repo_stars = top_repo['stargazers_count']

    languages = [repo['language'] for repo in repos if repo['language']]
    language_stats = Counter(languages)

    print(f"— Количество публичных репозиториев: {total_repos}")
    print(f"— Суммарное количество звёзд: {total_stars}")
    print(f"— Самый звёздный репозиторий: {top_repo_name} ({top_repo_stars} ⭐)")
    print("\n🔤 Наиболее часто используемые языки программирования:")

    for lang, count in language_stats.most_common():
        print(f"   {lang}: {count} репозиториев")


def main():
    """
    Основной цикл программы.
    """
    username = input('Введите имя пользователя GitHub: ').strip()
    print('Вывод программы: ')
    print('Аналитика профиля GitHub:', username)
    print('----------------------------------')

    repos = get_repos(username)
    analyze_repos(repos)


if __name__ == '__main__':
    main()




