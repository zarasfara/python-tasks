"""
    По заданной формуле члена ряда с номером k составить две программы:
    б) программу вычисления всех членов ряда, не меньших заданного числа E.

    Зачтено!
17) 2 / (k*(k+3))
"""

# E = float(input('Введите число E: '))
#
# k = 1
#
# formula = 2 / (k * (k + 3))  # 0.5
# if E <= 0:
#     print('Все члены ряда больше E. ')
# else:
#     if E > formula:
#         print('Все члены ряда меньше E')
#         exit()
#
#     print('Члены ряди больше E: ')
#     while E <= formula:
#         print(formula, end=', ')
#         k += 1
#         formula = 2 / (k * (k + 3))


# E = float(input('Введите число E: '))
# k = 1
#
# formula = 2 / (k * (k + 3))  # 0.5
# if E <= 0:
#     print('Все члены ряда больше E. ')
# else:
#     if E > formula:
#         print('Все члены ряда меньше E')
#     else:
#         print('Члены больше E: ')
#         for x in range(k, int(E)):
#             print(formula, end=', ')
#             k += 1
#             formula = 2 / (k * (k + 3))


# E = float(input('Введите число E: '))
#
# k = 1
#
# f = 2 / (k * (k + 3))
#
# if f < E <= 0:
#     print('Все члены ряда меньше E')
#     exit()
#
# print('Члены больше E: ')
# while E <= f:
#     print(f, end=', ')
#     k += 1
#     f = 2 / (k * (k + 3))
