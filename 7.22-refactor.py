"""
    Опишите, используя словарь, анкету школьника (фамилия, возраст).
    Определите возрастные группы в классе и напечатайте их списки.
"""

students_length = int(input('Введите кол-во учеников: '))

students = []

# Вводим студентов
for x in range(students_length):
    student = {'second_name': input('Введите фамилию ученика: '), 'age': int(input('Введите возраст ученика: '))}
    students.append(student)

# students = [
#     {
#         'name': 'Евгений',
#         'age': 14,
#     },
#     {
#         'name': 'Жока',
#         'age': 15,
#     },
#     {
#         'name': 'Вадим',
#         'age': 14,
#     },
#     {
#         'name': 'Артем',
#         'age': 21,
#     },
#     {
#         'name': 'Егор',
#         'age': 7,
#     },
# ]

age_groups = [8, 14, 18, 21]
age_groups.sort()

i = 0

# После каждой итерации i приравниваем значение age_group для создания промежутков,
# То есть в первый раз будет от 0 до 8 и т.д

for age_group in age_groups:

    print("Возрастная группа до или включительно: ", age_group)

    # Проходимся по студентам
    for student in students:

        if i < student['age'] <= age_group:
            print(student['second_name'], student['age'])

    i = age_group
