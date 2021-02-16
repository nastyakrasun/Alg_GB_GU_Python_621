"""
Задача2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
Решение:
"""
print('Сортировка по возрастанию методом слияния')
import random

SIZE = 15

def merge_sort(data):
    if len(data) < 2:
        return data
    else:
        mid = int(len(data) / 2)
        left_data = merge_sort(data[:mid])
        right_data = merge_sort(data[mid:])
        i = 0
        j = 0
        result = []
        while len(left_data) > i and len(right_data) > j:
                if left_data[i] < right_data[j]:
                    result.append(left_data[i])
                    i += 1
                else:
                    result.append(right_data[j])
                    j += 1
        while len(left_data) > i:  # эту часть кода понимаю, но додуматься до неё не могла
            result.append(left_data[i])
            i += 1
        while len(right_data) > j:
            result.append(right_data[j])
            j += 1

        return result

array = []
for i in range(SIZE):
    array.append(random.randint(0, 50))
print('Исходный массив: ', array)

#array2 = [10, 15, 2, 4, 7, 8, 16, 24, 29, 3, 35]  # пробный массив

print('Отсортированный массив: ', merge_sort(array))
