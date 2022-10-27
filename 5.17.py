"""

Найти наибольшие общие делители (НОД) для списка кортежей, составленных из пар чисел.

 Для нахождения НОД использовать функцию

"""

# list_of_tuples = [(50, 130), (2, 95), (3, 93)]

list_of_tuples = []

count_numbers = int(input("Введите количество пар чисел: "))

for x in range(count_numbers):
    w = []
    for y in range(1, 3):
        w.append(int(input(f"Введите {y}-ое число: ")))
    list_of_tuples.append(tuple(w))


def gcd(a, b):
    print(f"НОД Чисел {a} и {b} равно", end=" ", )

    # Пока а и b не равно 0
    while a != 0 and b != 0:
        if a > b:
            # В переменную а записываем остаток деления а на б
            a %= b
        else:
            # В переменную б записываем остаток деления б на а
            b %= a
    print(a + b)


for x in list_of_tuples:
    gcd(x[0], x[1])
