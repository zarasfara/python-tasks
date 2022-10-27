"""
Дано число N (N<=40). 
Составить программу нахождения всех делителей всех натуральных чисел от 1 до N
"""

# Зачтено

# Преобразуем в целочисленное ввод числа
N = int(input("Введите N: "))

# Проверка на то что число должно быть меньше 41
while N > 40:
    print("Число N должно быть меньше либо равно 40")
    N = int(input("Введите N: "))

# Создаем цикл
for i in range(1, N + 1):

    # Выводим на итерации i
    print("Делители числа", i, ":", end=" ")

    j = 1
    # цикл
    for j in range(1, i + 1):
        # проверяем что число делится без остатка
        if i % j == 0:
            if j == i:
                print(j)
            else:
                print(j, end=', ')
        j += 1
