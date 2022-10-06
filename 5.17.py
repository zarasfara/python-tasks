"""

Найти наибольшие общие делители (НОД) для списка кордежей, составленных из пар чисел.

 Для нахождения НОД использовать функцию

"""
import math


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(a + b)


list_of_tuples = [(50, 130), (2, 95), (3, 93)]

for x in list_of_tuples:
    gcd(x[0], x[1])

# for x in list_of_tuples:
#     print(math.gcd(x[0], x[1]))
