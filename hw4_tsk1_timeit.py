"""
ПЗ3, задача4 (Определить, какое число в массиве встречается чаще всего)
(- если несколько чисел одинаково часто встречаются в массиве
- цикл for выводит только одно из этих чисел
- массив не любой, а в отрезке [0, 100]
- за параметр изменения беру длинну массива
- использую в качестве второго решения решение преподавателя со словарём)
прикидывание графика у алгоритма
"""
import random
import timeit

# вариант 1 с обращением по индексу и вложенными циклами
def func_max_input1(size):
    array = [random.randint(0, 100) for _ in range(size)]
    a = array[0]  # предполагаемое число, которое встречается в массиве чаще всего
    max_frequency = 1
    for i in range(len(array)):
        frequency = 1
        for f in range(i + 1, len(array)):
            if array[i] == array[f]:
                frequency += 1
        if frequency > max_frequency:
            max_frequency = frequency
            a = array[i]

    if max_frequency == 1:
        return('Каждое число входит в массив по 1 разу')
    else:
        return(f'Число {a} встречается в массиве чаще всего')

print(timeit.timeit('func_max_input1(10)', number = 100, globals=globals()))  # 0.0021194000000000005
print(timeit.timeit('func_max_input1(100)', number = 100, globals=globals()))  # 0.0539799
print(timeit.timeit('func_max_input1(1000)', number = 100, globals=globals()))  # 4.2579021

# решение преподавателя
# ваниант 2 со словарём
def func_max_input2(size):
    array = [random.randint(0, 100) for _ in range(size)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return f'Число {num} встречется {frequency} раз(а)'
    else:
        return 'Все элементы уникальны'

print(timeit.timeit('func_max_input2(10)', number = 100, globals=globals()))  # 0.0014525000000000024
print(timeit.timeit('func_max_input2(100)', number = 100, globals=globals()))  # 0.0151656(9)
print(timeit.timeit('func_max_input2(1000)', number = 100, globals=globals()))  # 0.1500994

# вывод: вариант решения 2 (со словарём) имеет один цикл (предполагается линейная асимптотика),
# по данным timeit вариант 2 наиболее оптимален по времени
# (вариант 1 имеет 2 вложенных цикла, предполагается асимптотика О(n**2) или параболическая
# при увеличении размера массива время выполнения алгоритма увеличевается согласно закономерности О(n**2))
