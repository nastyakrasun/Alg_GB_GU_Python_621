"""
Задача1.В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Решение:
"""

MIN_ITEM_N = 2  # нижняя граница диапазона натуральных чисел
MAX_ITEM_N = 100  # верхняя граница диапазона натуральных чисел
MIN_ITEM_D = 20  # нижняя граница диапазона делителей
MAX_ITEM_D = 90  # верхняя граница  диапазона делителей

array = list(range(MIN_ITEM_N, MAX_ITEM_N))  # массив натуральных делимых
divisor = [0] * (MAX_ITEM_D - MIN_ITEM_D + 1)  # массив диапазона делителей

for n in range(MIN_ITEM_N, MAX_ITEM_N):
    for d in range(MIN_ITEM_D, MAX_ITEM_D):
       if n % d == 0:  # если число кратно делителю
           divisor[d - MIN_ITEM_D] += 1  # диапазон кратных делителю чисел увеличивается на 1

print(f'Кратность чисел в диапазоне от {MIN_ITEM_N} до {MAX_ITEM_N} числам в диапазоне от {MIN_ITEM_D} до {MAX_ITEM_D}.')
for d in range(MIN_ITEM_D, MAX_ITEM_D):
    print(f'Чисел, кратных {d}: {divisor[d - MIN_ITEM_D]}.')
