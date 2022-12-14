"""
    Опишите, используя словарь, анкету школьника (фамилия, возраст).
    Определите возрастные группы в классе и напечатайте их списки.
"""
students = dict()

student_counter = int(input("Введите кол-во учеников: "))

for i in range(0, student_counter):

    student_age = int(input("Введите возраст: "))
    student_second_name = input("Введите фамилия: ")

    # Если в группе студентов нет такого ключа, то создаем его с пустым списком
    if students.get(student_age) is None:
        students[student_age] = []

    # Добавляем ученика
    students[student_age].append(student_second_name)


age_groups = [int(input("Введите возрастную группу "))
              for _ in range(0, int(input("Введите кол-во групп: ")))]

# возраст начала школьного обучения – не ранее 7 лет
i = 7

for age in age_groups:

    for student_age in students:

        # Если возраст студента больше прошлой группы и меньше текущей для сравнения - выводим
        if i < student_age <= age:
            for student in students[student_age]:
                print(f"{student} в группе от {i} до {age} включительно")
    i = age
