"""
    Дана строка. 
    Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.
"""

# Зачтено

englishAlphabet = "qwertyuiopasdfghjklzxcvbnm"  # все строчные буквы
russianAlphabet = "йцукенгшщзхфъывапролджэячсмитьбю"  # все строчные буквы

q = input("Введите строку: ")  # наша строка

russianWords = 0
latinWords = 0

for i in q:

    if i in englishAlphabet:
        latinWords += 1

    elif i in russianAlphabet:
        russianWords += 1

print("Русских букв: ", russianWords)
print("Английских букв: ", latinWords)
