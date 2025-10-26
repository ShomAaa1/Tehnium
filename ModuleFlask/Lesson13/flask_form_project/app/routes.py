from flask import render_template, request, redirect, url_for
import random
from app import app


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name') # Получаем имя из формы
        email = request.form.get('email') # Получаем email из формы
        color = request.form.get('color')
        job = request.form.get('job')
        hobbies = request.form.getlist('hobby')
        level = request.form.get('level')

        jokes = [
            'Почему программисты не любят природу? - В ней слишком много багов 🐛',
            'Я не ленива, я просто в режиме энергосбережения ⚡',
            'Ошибка 404: мотивация не найдена 😅',
            'Зачем программист пошел в бар? - Чтобы обновить кэш 🍺',
            'Код без комментариев - как квест без карты 🗺'
        ]

        random_joke = random.choice(jokes)

        return render_template('result.html', name=name, email=email,
                               color=color, job=job, hobbies=hobbies, level=level,
                               joke=random_joke)
    else:
        return redirect(url_for('form')) # Если запрос GET, возвращаем на форму
