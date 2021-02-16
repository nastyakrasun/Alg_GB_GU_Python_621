""" https://drive.google.com/file/d/1NwoqoIFo9Es6LYBmAQJNmTXIJM4MViyA/view?usp=sharing
Задача2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
Решение: (считаю количество повторений для каждой цифры,
например, в числе 3345600 4 четные цифры (4, 6 и 0) и 3 нечетные (3 и 5))
"""
n = []
even = []
odd = []

print('Количество чётных и нечётных цифр натурального числа')
num = int(input('Введите число: '))

while num > 0:
    n.append(num % 10)
    num = num // 10

for i in range(len(n)):
        if int(n[i]) % 2:
            odd.append(n[i])
        else:
            even.append(n[i])

print(f'В данном числе чётных цифр: {len(even)}.')
print(f'Нечётных цифр: {len(odd)}.')
