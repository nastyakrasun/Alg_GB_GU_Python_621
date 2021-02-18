"""
Задача4. Определить, какое число в массиве встречается чаще всего.
Решение:
(если несколько чисел одинаково часто встречаются в массиве,
цикл for выведет только одно из этих чисел;
комментарии-строки - проверяла на "нужном мне" массиве)
"""
import random

SIZE = 20
MIN_ITEM = -5  # нижняя граница диапазона целых чисел
MAX_ITEM = 5  # верхняя граница диапазона целых чисел

print('Какое число в массиве встречается чаще всего?')
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # генерируем массив случайных целых чисел
#array = [15, 0, 0, 12, 45, 100, 52, 84, 200, 12, 0, 45, 78]
print(f'Исходный массив: {array}.')

a = array[0]  # предполагаемое число, которое встречается в массиве чаще всего
max_frequency = 1

for _ in range(SIZE):
#for _ in range(len(array)):
    frequency = 1
    for f in range(_ + 1, SIZE):
    #for f in range(_ + 1, len(array)):
        if array[_] == array[f]:
            frequency += 1
    if frequency > max_frequency:
        max_frequency = frequency
        a = array[_]

if max_frequency == 1:
    print('Каждое число входит в массив по 1 разу.')
else:
    print(f'Число {a} встречается в массиве чаще всего.')
    #print(f'{max_frequency} раз(а).')
