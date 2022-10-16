"""
Дан символьный файл f.
Группы слов, разделенных пробелами (одним или несколькими) и не содержащие пробелов внутри себя, будем называть словами.
Удалить из файла все однобуквенные слова и лишние пробелы. Результат записать в файл g.
"""
import re

document = open('f.txt', 'r', encoding='utf-8').readlines()
second_document = open('g.txt', 'w', encoding='utf-8')

# shalom = re.sub(r'\s+', ' ', document).split(' ')
# document[document.index(row)] = re.sub(r'\s+', ' ', document[document.index(row)])

q = []
for row in document:
    q += re.split(r'\s+', row)
q.remove('')

c = ' '.join(str(e) for e in q)
# for x in q:
    # if len(x) == 1:
second_document.write(c)