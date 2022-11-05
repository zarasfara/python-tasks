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

# Берем элементы с элемента 7 по 10
second_new_list = sourceList[6:10]
# Сортировка
first_new_list.sort()
second_new_list.sort(reverse=True)

# Удаляем у исходного списка элементы
del sourceList[0:4]
del sourceList[2:6]

# Объединяем списки
print("Список после преобразования ", first_new_list + sourceList + second_new_list)
