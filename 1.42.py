"""
1.42 Найти сумму первой и последней цифр любого целого положительного числа.
"""
# Зачтено

# Вводим число
number = input("Введите, число: ")

# Выводим сумму первой и первой цифры
print("Сумма первого и последнего элемента числа равна: ", int(number[0]) + int(number[-1]))
