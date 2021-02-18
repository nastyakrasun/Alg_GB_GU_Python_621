"""
https://drive.google.com/file/d/1JvlJ_4tirUwTRzeE24R2Pd_hhIzX4jCi/view?usp=sharing
Задача9. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
Решение:
"""
print('Определение среднего из трёх введённых разных чисел')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if (a > b and a < c) or (a < b and a > c):
    print(f'{a} - среднее число.')
elif (a < b and a < c and b > c) or (a > b and a > c and b < c):
    print(f'{c} - среднее число.')
else:
    print(f'{b} - среднее число.')
