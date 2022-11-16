"""
Дан символьный файл f.
Группы слов, разделенных пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем называть словами.
Удалить из файла все одно буквенные слова и лишние пробелы. Результат записать в файл g.
"""
# Ввод слов/символов в файл руками
# Проверка на то что ничего не ввели

import re

# Открываем на запись
second_document = open('g.txt', 'w', encoding='utf-8')

with open('f.txt', 'w+', encoding='utf-8') as f:
    # вводим слова
    words = input("Введите слова через пробел: ")

    # Если что-то ввели
    if len(words) != 0:
        # сплитим строку по пробелам любой длинной
        for line in re.split("\s+", words):

            # Если длина слова равна 1 - пропускаем
            if len(line) == 1:
                continue

            # Запись в файл
            f.write(line + ' ')
    else:
        print("Ничего не ввели")

with open('f.txt', 'r', encoding='utf-8') as f:
    # Разделяем и читаем строку по переносам строки
    for line in f.read().split('\n'):
        a = second_document.write(' '.join(filter(lambda x: len(x) != 1, line.split())) + '\n')
        print(a)
