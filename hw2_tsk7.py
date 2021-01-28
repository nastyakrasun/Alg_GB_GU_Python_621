"""
Задача7. Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
Решение:
"""
def add_recursion(a): # определяем рекурсивную функцию суммы ряда натуральных чисел
    if a <= 1:
        return a
    return a + add_recursion(a - 1)

def mult_func(b):  # определяем функцию для заданной формулы вычисления произведения
    if b == 1:
        return b
    return b * (b + 1) / 2

print('Программа, проверяющая равенство 1+2+...+n = n(n+1)/2 для всех натуральных чисел')
n = int(input('Введите любое натуральное число: '))

print(f'1+2+...+n = {add_recursion(n)}')
print(f'n(n+1)/2 = {mult_func(n)}')

if add_recursion(n) == mult_func(n):
    print('равенство верно')
else:
    print('равенство неверно')
# работает и для 0