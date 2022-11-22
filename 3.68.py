"""
    Дан список из 10 элементов. Первые 4 упорядочить по возрастанию, последние 4 по убыванию.
"""

sourceList = []

# Ввод чисел
for x in range(10):
    num = int(input('Введите число: '))
    sourceList.append(num)

# Исходный список
print("Изначальный список ", sourceList)

# Берем элементы с элемента 0 по 4
first_new_list = sourceList[0:4]
sourceList = sorted(sourceList[0:4]) + sourceList[4:6] + sorted(sourceList[6:10], reverse=True)

print("Изменённый список ", sourceList)
