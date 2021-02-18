"""
Задача: подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Решение:
версия и разрядность ОС и интерпретатора Python: platform.architecture() --> ('64bit', 'WindowsPE')
создали универсальный код для замера памяти = списали из вебинара 6.
"""

import sys
from decimal import Decimal
import random

def show(obj):
    print(f'{type(obj)=}\t{sys.getsizeof(obj)=}\t{obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items:
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)

"""
ПЗ3, задача3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Решение:
"""
print('ПЗ3 Задача3')
SIZE = 15  # изменение sys.getsizeof(obj) зависит от длины массива (на практике подтверждается)
MIN_ITEM = -100  # нижняя граница диапазона целых чисел
MAX_ITEM = 100  # верхняя граница диапазона целых чисел
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]  # генерируем массив случайных целых чисел

print('В массиве случайных целых чисел меняем местами минимальный и максимальный элементы.')
#array = [0, 0, 12, 45, 100, 52, 84, 200, 12, 0, 45, 78]
print(f'Исходный массив: {array}.')
show(array)

min_elem = 0  # предполагаемый индекс минимального элемента
max_elem = 0  # предполагаемый индекс максимального элемента

for i in range(len(array)):
    if array[i] < array[min_elem]:
        min_elem = i
    elif array[i] > array[max_elem]:
        max_elem = i

spam = array[min_elem]  # вспомогательная переменная
array[min_elem] = array[max_elem]
array[max_elem] = spam

print(f'Полученный массив: {array}.')
show(array)

# Вывод: количество выделенных переменных памяти под массив целых чисел зависит от длины массива:
# size = 5 sys.getsizeof(obj)=120
# size = 15 sys.getsizeof(obj)=184
# и т.д.
# оно не зависит от способа задания массива:
# вручную или с помощью функции random.randint (random.randrange так же рассматривала, другие задачи с массивами тоже брала)

""" ПЗ1, задача1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
print('ПЗ1 Задача1')
a = input('Введите число: ')

print('тип integer')
summ_int = 0
show(summ_int)
mult_int = 1
show(mult_int)

for n in a:
    summ_int += int(n)
    mult_int *= int(n)
print(f'Сумма цифр числа {a} равна {summ_int}.')
show(summ_int)
print(f'Произведение цифр числа {a} равно {mult_int}.')
show(mult_int)

print('тип float')
summ_float = float(0)
show(summ_float)
mult_float = float(1)
show(mult_float)

for n in a:
    summ_float += float(n)
    mult_float *= float(n)
print(f'Сумма цифр числа {a} равна {summ_float}.')
show(summ_float)
print(f'Произведение цифр числа {a} равно {mult_float}.')
show(mult_float)

print('тип decimal')
summ_decimal = Decimal(0)
show(summ_decimal)
mult_decimal = Decimal(1)
show(mult_decimal)

for n in a:
    summ_decimal += Decimal(n)
    mult_decimal *= Decimal(n)
print(f'Сумма цифр числа {a} равна {summ_decimal}.')
show(summ_decimal)
print(f'Произведение цифр числа {a} равно {mult_decimal}.')
show(mult_decimal)

# Вывод: количество выделенных переменных памяти под число зависит от типа числа:
# type(obj)=<class 'int'>	sys.getsizeof(obj)=28
# type(obj)=<class 'float'>	sys.getsizeof(obj)=24
# type(obj)=<class 'decimal.Decimal'>	sys.getsizeof(obj)=104
# Но задача про целые числа.
# наиболее эффективно память используется при типе float, так как:
# * знаки после запятой не рассматриваются - задача предполагает, что их нет
# * предполагается, что для слишком больших чисел данная программа использоваться не будет
# * если нужна большая точность - для данных задачи предпочтителен тип int
