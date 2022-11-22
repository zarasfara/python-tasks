"""
Дан символьный файл f.
Группы слов, разделенных пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем называть словами.
Удалить из файла все одно буквенные слова и лишние пробелы. Результат записать в файл g.
"""
# Ввод слов/символов в файл руками
# Проверка на то что ничего не ввели

# Открываем на запись
second_document = open('g.txt', 'w', encoding='utf-8')

with open('f.txt', 'w', encoding='utf-8') as f:
    # вводим слова
    words = input("Введите слова через пробел: ")

    if len(words) == 0:
        print("Вы ничего не ввели")
        exit()

    f.write(' '.join(filter(lambda x: len(x) != 1, words.split())).strip())

with open('f.txt', 'r', encoding='utf-8') as f:

    for line in f.read():
        second_document.write(line)
