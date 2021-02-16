"""
Задача1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
Решение:
"""
print('Сортировка по убыванию методом пузырька')
import random

def bubble1_conv_sort(data):  # алгоритм сортировки в виде функции, которая принимает на вход массив данных
    spam = 1
    while spam < len(data):
        for i in range(len(data) - 1):
            if data[i] < data[i+1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        spam += 1
        #print(data)

def bubble2_conv_sort(data):  # изменённый алгоритм для сортировки пузырьком
    # (прочла про сортировку шейкером и расческой, поняла что это)
    for k in range(len(data) - 1):
        for i in range(len(data) - k - 1):
            if data[i] < data[i+1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        #print(data)

def bubble3_conv_sort(data):  # ещё 1 вариант
    for k in range(len(data) - 1):
        for i in range(len(data) - k - 1):
            if data[i] < data[i+1]:
                spam = array[i]
                data[i] = data[i+1]
                data[i + 1] = spam
        #print(data)

array = [i for i in range(-100, 100)]  # range(MIN_VAL, MAX_VAL) при заранее заданных MIN_VAL, MAX_VAL
array == random.shuffle(array)

#array = [-9, 4, 1, 2, -10, -2, 9, -3, 7, -4, 5, 3, -8, -6, -7, 0, 6, 8, -5, -1]  # пробный массив

bubble1_conv_sort(array)
print('отсортированный массив, вариант 1: ',array, sep='\n')
array == random.shuffle(array)
bubble2_conv_sort(array)
print('отсортированный массив, вариант 2: ',array, sep='\n')
array == random.shuffle(array)
bubble3_conv_sort(array)
print('отсортированный массив, вариант 3: ',array, sep='\n')
