"""
Дан символьный файл f.
Группы слов, разделенных пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем называть словами.
Удалить из файла все однобуквенные слова и лишние пробелы. Результат записать в файл g.
"""
import re

document = open('f.txt', 'r', encoding='utf-8').read()
second_document = open('g.txt', 'w', encoding='utf-8')

for line in document.split('\n'):
    second_document.write(' '.join(filter(lambda x: len(x) != 1, line.split())) + ' \n')

"""
chelovek orange  orange a stupid b kind test mobile rea tesla
wer rew человек
"""
