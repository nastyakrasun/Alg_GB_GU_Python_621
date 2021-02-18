"""
Задача1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
Решение:
"""
import hashlib

def func(str_):
    hash_ = []  # массив из хешей
    subs = []  # массив из различных подстрок строки str_

    for len_sub in range(1, len(str_)):  # len_sub - длина подстроки (от 1 - чтобы не включать пустую строку и строку целиком(22) - "элементарно")
        for i in range(len(str_) - len_sub + 1):
            new_hash = hashlib.sha1(str_[i:i+len_sub].encode('utf-8')).hexdigest()
            if new_hash in hash_:
                break
            else:
                hash_.append(new_hash)
                subs.append(str_[i:i+len_sub])

    return len(subs)

print('Определение количества различных подстрок с использованием хеш-функции.')
a = input('Введите строку: ')

print(func(a))
