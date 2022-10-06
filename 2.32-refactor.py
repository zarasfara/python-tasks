"""
    Во введенной строке удалить пробелы между первым и вторым вопросительным знаком
"""

# привет крутой человек? как  дела ? Дети играют во дворе ?
string = input('Введите строку: ')

# Первое вхождение знака
start = string.find('?')

# Строка от первого знака до второго
var = string[start: string.find('?', start + 1)].replace(' ', '')

# Строка до первого знака
first_string = string[:start]

# Строка после второго знака
second_string = string[string.find('?', start + 1):]

# Конкатенация
print(first_string + var + second_string)
