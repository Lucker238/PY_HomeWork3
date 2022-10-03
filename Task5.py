# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def makeFibonachchiList(number):
    number = int(number)
    result = [0] * (number * 2 + 1)
    if number:
        result[number+1] = 1
        result[number-1] = -1
        index = 2
        while index <= number:
            result[number+index] = result[number+index-1] + result[number+index-2]
            result[number-index] = result[number-index+1] + result[number-index+2]
            index += 1
    return result

print(makeFibonachchiList(input('Введите число: ')))