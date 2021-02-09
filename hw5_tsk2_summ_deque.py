"""
Задача2.Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Решение:
"""
from collections import deque

def to_num(array):
    for i in range(len(array)):
        if array[i] == 'A':
            array[i] = 10
        elif array[i] == 'B':
            array[i] = 11
        elif array[i] == 'C':
            array[i] = 12
        elif array[i] == 'D':
            array[i] = 13
        elif array[i] == 'E':
            array[i] = 14
        elif array[i] == 'F':
            array[i] = 15
        # else:
        # array[i] = int(array[i])  # не знаю, как вообще обойтись без int
        elif array[i] == '0':
            array[i] = 0
        elif array[i] == '1':
            array[i] = 1
        elif array[i] == '2':
            array[i] = 2
        elif array[i] == '3':
            array[i] = 3
        elif array[i] == '4':
            array[i] = 4
        elif array[i] == '5':
            array[i] = 5
        elif array[i] == '6':
            array[i] = 6
        elif array[i] == '7':
            array[i] = 7
        elif array[i] == '8':
            array[i] = 8
        elif array[i] == '9':
            array[i] = 9
        i += 1
    return array

def to_sixteen(array):
    for i in range(len(array)):
        if array[i] == 10:
            array[i] = 'A'
        elif array[i] == 11:
            array[i] = 'B'
        elif array[i] == 12:
            array[i] = 'C'
        elif array[i] == 13:
            array[i] = 'D'
        elif array[i] == 14:
            array[i] = 'E'
        elif array[i] == 15:
            array[i] = 'F'
        # else:
        # array[i] = int(array[i])  # не знаю, как вообще обойтись без int
        elif array[i] == 0:
            array[i] = '0'
        elif array[i] == 1:
            array[i] = '1'
        elif array[i] == 2:
            array[i] = '2'
        elif array[i] == 3:
            array[i] = '3'
        elif array[i] == 4:
            array[i] = '4'
        elif array[i] == 5:
            array[i] = '5'
        elif array[i] == 6:
            array[i] = '6'
        elif array[i] == 7:
            array[i] = '7'
        elif array[i] == 8:
            array[i] = '8'
        elif array[i] == 9:
            array[i] = '9'
        i += 1
    return array

def summ(a, b):
    c = deque([])
    for i in range(len(a)):
        c.append(a[i] + b[i])  # если через список, insert(i, a[i] + b[i])
        # единств отличие deque от list (которое я нашла в своём коде) - понимать, где append, где appendleft - долго искала
        # может, с deque быстрее работает программа...
    for i in range(len(c)):
        if c[i] // 16 != 0:
            c[i - 1] = c[i - 1] + (c[i] // 16)
            c[i] = (c[i] % 16)
        """
        else:
            if c[i] >= 16:
                c[i - 1] = c[i - 1] + 1  # здесь нужно что-то типа рекурсии, чтобы проверять с[i-1] на кратность 16 
                # верно не посчитает даже F+FF 
                c[i] = 0
        """
    return c

print('Программа сложения двух шестнадцатеричных чисел')

a = deque(input('Первое слагаемое: '))  # делала со списком list
b = deque(input('Второе слагаемое: '))
#print(a, b, sep='\n')
if len(a) < len(b):
    while len(a) < len(b) + 1:
        a.appendleft('0')  # вставляла через insert(0, '0')
    while len(b) < len(a):
        b.appendleft('0')
else:
    while len(b) < len(a) + 1:
        b.appendleft('0')
    while len(a) < len(b):
        a.appendleft('0')
#print(a, b, sep='\n')

a = to_num(a)
b = to_num(b)
#print(summ(a,b))

print('Сумма равна: ', *to_sixteen(summ(a,b)))
