"""
https://drive.google.com/file/d/1lFzSEYxJTxKSrhIYX-rBuAw-zwQ6f5VN/view?usp=sharing
Задача8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
Решение:
"""
print('Високосный ли год?')

year = int(input('Введите год полностью: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} год високосный.')
        else:
            print(f'{year} год не является високосным.')
    else:
        print(f'{year} год високосный.')
else:
    print(f'{year} год не является високосным.')
