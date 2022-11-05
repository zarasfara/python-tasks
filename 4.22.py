"""
    В классе учится n учеников. Известны их имена.
    Известно так же кто был в гостях у Кати, кто был у Васи и т.д.
    Определить, есть ли в классе хотя бы один человек, который не был в гостях ни у кого из своих одноклассников.
    Если есть такие ученики, то вывести их имена, если нет, то сообщить об этом.

    Использовать множество
"""

# Список словарей
students = [
    {
        'name': 'Евгений',
        'guest_kate': True,
        'guest_vasya': True,
    },
    {
        'name': 'Вадим',
        'guest_kate': True,
        'guest_vasya': True,
    },
    {
        'name': 'Максим',
        'guest_kate': True,
        'guest_vasya': True,
    },
    {
        'name': 'Егор',
        'guest_kate': False,
        'guest_vasya': False,
    }
]

# students = []

# n = int(input("Введите кол-во учеников"))

# for i in range(n):
#     student = {'name': input('Введите имя студента'), 'guest_vasya': input('Был ли он гостем Васи'), 'guest_kate': input('Был ли он гостем Кати')}
#     students.append(student)


for student in students:
    # Проверяем что ученик был в гостях хоть у кого-то
    if student['guest_vasya'] is True or student['guest_kate'] is True:
        print(student['name'] + " был у кого-то в гостях")

        # Иначе сообщаем что он не был в гостях
    else:
        print(student['name'] + " не был в гостях ни у кого из своих одноклассников")
