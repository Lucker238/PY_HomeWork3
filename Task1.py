# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def createList(len):
    array = []
    for i in range(0,int(len)):
        array.append(random.randint(1,9))
    return array

def findSum(array):
    sum = 0
    for i in range(0, len(array)):
        if i % 2:
            sum += array[i]
    return sum

array = createList(input('Введите длину списка чисел: '))
print(array)
print(findSum(array))
