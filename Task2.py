# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

def createList(len):
    result = []
    for i in range(0,int(len)):
        result.append(random.randint(1,9))
    return result

def findProd(array):
    result = []
    for i in range(0, (len(array)+1) // 2):
        result.append(array[i] * array[-(i+1)])
        print(f'{array[i]}*{array[-(i+1)]}={result[i]}')
    return result

array = createList(input('Введите длину списка чисел: '))
print(array)
print(findProd(array))