"""
    Опишите, используя словарь, анкету школьника (фамилия, возраст).
    Определите возрастные группы в классе и напечатайте их списки.
"""
students = dict()

for i in range(0,2):

    student_age =  int(input("Введите возраст: "))
    student_second_name = input("Введите фамилия: ")

    # Если в группе студентов нет такого ключа, то создаем его с пустым списком
    if students.get(student_age) is None:
        students[student_age] = []

    #Добавляем ученика
    students[student_age].append(student_second_name)


age_groups = [int(input("Введите возрастную группу ")) for _ in range(0, int(input("Введите кол-во групп: ")))]

# возраст начала школьного обучения – не ранее 7 лет
i = 7


for age in age_groups:

    for student_age in students:

        # Если возраст студента меньше прошлой группы и больше текущей для сравнения - выводим
        if i < student_age <= age:
            print(f"{students[student_age]} в группе от {i} до {age} включительно")
    i = age

# for age in range(0,len(age_groups)):

#     for student_age in students:

#         if i < student_age <= age_groups[age]:
#             print(f"{students[student_age]} в группе от {i} до {age_groups[age]} включительно")
#     i = age_groups[age]

