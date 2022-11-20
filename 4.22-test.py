"""
    В классе учится n учеников. Известны их имена.
    Известно так же кто был в гостях у Кати, кто был у Васи и т.д.
    Определить, есть ли в классе хотя бы один человек, который не был в гостях ни у кого из своих одноклассников.
    Если есть такие ученики, то вывести их имена, если нет, то сообщить об этом.

    Зачтено!
    Использовать множество
"""

# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

"""
    Можно сделать вместо множества у детей сначала сделать список пустой
    А потом случайно его заполнять или явно указывать кто был у кого
"""

kate = ('Катя', {
    'Женя',
    'Миша'
})

petya = ('Петя', {
    'Женя',
    'Андрей'
})

count_students = int(input("Введите количество учеников: "))
students = []

for student in range(count_students):
    student_name = input("Введите имя: ")
    students.append(student_name)


students = set(students)

intersection_students = students.intersection(kate[1], petya[1])

if len(intersection_students) != 0:
    for student in intersection_students:
        print(f"{student} Был у Кати и у Пети")
else:
    print("Никто у Кати и у Пети не был")
