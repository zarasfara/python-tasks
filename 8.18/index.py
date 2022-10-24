"""
Дан символьный файл f.
Группы слов, разделенных пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем называть словами.
Удалить из файла все однобуквенные слова и лишние пробелы. Результат записать в файл g.
"""
import re

document = open('f.txt', 'r+', encoding='utf-8')
second_document = open('g.txt', 'w', encoding='utf-8')

q = []
for row in document:
    q += re.split(r'\s+', row)

for row in q:

    if row == '':
        q.remove('')

    if len(row) == 1:
        q.remove(row)

c = ' '.join(str(e) for e in q)

second_document.write(c)

"""
chelovek orange  orange a stupid b kind test mobile rea tesla
wer rew человек
"""
