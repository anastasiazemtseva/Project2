#Тест "Как хорошо ты знаешь Гарри Поттера"
quantity = 0

print('Давай узнаем как хорошо ты знаешь вселенную Гарри Поттара')
print('1. Сколько лет длится обучение в Хогвартсе?')
print('Врианты ответов:')
print('a) 7 лет;')
print('b) 10 лет;')
print('c) 5 лет;')
print('Ваш ответ:')
answer = input()

if answer == 'a':
    quantity = quantity+1
    print('Молодец! Это правильный ответ.')
else:
    print('Гарри учился в Хогвартсе 7 лет, как и остальные студенты.')
    pass
print()

print('2. Кем Гарри Хотел стать после окончания учебы в Хогвартсе?')
print('Врианты ответов:')
print('a) Профессиональным игроков в квиддич;')
print('b) Мракоборцем;')
print('c) Министром Магии;')
print('Ваш ответ:')
answer = input()

if answer == 'b':
    quantity = quantity+1
    print('Действительно, Гарри хотел стать мракоборцем.')
else:
    print('Увы! Гарри хотел быть Мракоборцем')
    pass
print()

print('3. Как Гарри никогда не называли?')
print('Врианты ответов:')
print('a) Грязнокровка;')
print('b) Избранный;')
print('c) Нежелательно лицо №1;')
print('Ваш ответ:')
answer = input()

if answer == 'a':
    quantity = quantity+1
    print('Молодец! Гарри Поттер является чистокровным волшебником. '
          'Его никогда не называли Грязнокровкой.')
else:
    print('Гарри Поттер является чистокровным волшебником. '
          'Его никогда не называли Грязнокровкой.')
    pass
print()

print('4. Какое варенье больше всего любил Дамблдор?')
print('Врианты ответов:')
print('a) Малиновое;')
print('b) Вишневое;')
print('c) Яблочное;')
print('Ваш ответ:')
answer = input()

if answer == 'a':
    print('Молодец! Ты правильно ответил!')
    quantity = quantity+1
else:
    print('Любимое варенье Дамблдора - малиновое.')
    pass
print()

print('5. Патронус Гермионы это?')
print('Врианты ответов:')
print('a) Собака;')
print('b) Выдра;')
print('c) Лиса;')
print('Ваш ответ:')
answer = input()

if answer == 'b':
    quantity = quantity+1
    print('Да! Патронус Гермионы - Выдра.')
else:
    print('Увы! Патронус Гермионы - Выдра.')
    pass
print()

print('6. Как зовут самого старшего Брата Рона?')
print('Врианты ответов:')
print('a) Билл;')
print('b) Фред;')
print('c) Чарли;')
print('Ваш ответ:')
answer = input()

if answer == 'a':
    quantity = quantity+1
    print('Правильно!')
else:
    print('Фред и Чарли его старшие братья, а вот Билл самый старший!')
    pass
print()

print('7. Что Дамблдор оставил Гермионе в своем завещании?')
print('Врианты ответов:')
print('a) Снитч;')
print('b) Сказки Барда Бидля;')
print('c) Делюминатор;')
print('Ваш ответ:')
answer = input()

if answer == 'b':
    quantity = quantity + 1
    print('Молодец! Это правильный ответ!')
else:
    print('Увы! Делюминатор Дамблдор оставил Рону, а снитч вообще ему'
          ' не принадлежал. Правильный ответ - Сказки Барда Бидля.')
    pass
print()

print('8. Фестралов могут видеть люди, которые видели...')
print('Врианты ответов:')
print('a) Дементора;')
print('b) Смерть;')
print('c) Волан-де-Морта;')
print('Ваш ответ:')
answer = input()

if answer == 'b':
    quantity = quantity+1
    print('Я смотрю, ты действительно поттерман.')
else:
    print('Главная отличительная особенность фестралов в том, '
          'что их может видеть только человек, познавший смерть,'
          'для других людей они остаются невидимыми.')
    pass
print()

print('9. В каком году Дамблдор победил Грин-де-Вальда?')
print('Врианты ответов:')
print('a) 1945;')
print('b) 1910;')
print('c) 1990;')
print('Ваш ответ:')
answer = input()

if answer == 'a':
    quantity = quantity+1
    print('У тебя хорошая память!')
else:
    print('Увы! Дамблдор победил Грин-де-Вальда в 1945 году.')
    pass
print()

print('10. Какое живое существо изображено на гербе Пуффендуя')
print('Врианты ответов:')
print('a) Дракон;')
print('b) Барсук;')
print('c) Собака;')
print('Ваш ответ:')
answer = input()

if answer == 'b':
    quantity = quantity+1
    print('Да! Барсук действительно является символом Пуффендуя.')
else:
    print('На самом деле на гербе изображен барсук.')
    pass
print()
print('Твой результат:', quantity)
if 8 <= quantity <= 10:
    print('Ты настоящий поттерман. '
          'Знаешь абсолютно все про мир Гарри Поттера.')
elif 5 < quantity < 8:
    print('Молодец! Не плохой результат! '
          'Ты занешь много фактов о поттериане. Это достойно похвалы!')
else:
    print('К сожалению тебе не удалось правильно ответить на многие '
          'вопросы, но не расстраивайся, попробуй пройти этот тест заново!')