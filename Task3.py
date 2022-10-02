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
    result = 0

    
