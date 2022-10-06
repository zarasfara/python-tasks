"""
    Дан список из 10 элементов. Первые 4 упорядочить по возрастанию, последние 4 по убыванию.
"""

sourceList = []

# Ввод чисел
for x in range(9):
    num = int(input('Введите число: '))
    sourceList.append(num)

# Исходный список
print("begin ", sourceList)

# Берем элементы с элемента 0 по индексу по 4
new_list = sourceList[0:4]

# Берем элементы с элемента 7 по индексу по 10
new_list2 = sourceList[6:10]
# Сортировка
new_list.sort()
new_list2.sort(reverse=True)

# Удаляем у исходного списка элементы
del sourceList[0:4, 2:6]
del sourceList[2:6]

# Объединяем списки
print(new_list + sourceList + new_list2)
