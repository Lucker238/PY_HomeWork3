# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def magicTransformation(number):
    number = int(number)
    result = ''
    while number >= 2:
        result += str(number % 2)
        number = number // 2
    return (result+str(number))[::-1]

print(magicTransformation(input('Введите число: ')))
