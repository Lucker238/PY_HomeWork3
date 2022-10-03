# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

def createList(len):
    result = []
    for i in range(0,int(len)):
        result.append(round(random.uniform(1,50),2))
    return result

def findDifference(array):
    minn = array[0] % 1
    maxx = array[0] % 1
    for i in array:
        if i % 1 > maxx:
            maxx = i % 1
        elif 0 < i % 1 < minn:
            minn = i % 1
    print(f'{round(maxx,2)}-{round(minn,2)}',end='=')
    return round(maxx - minn,2)


array = createList(input('Введите длину массива чисел: '))
print(array)
print(findDifference(array))

    
