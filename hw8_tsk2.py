"""
Задача2) Закодируйте любую строку по алгоритму Хаффмана.
Решение: скачивала учебную библиотеку binarytree, разбиралась в сути алгоритма на примере конкретной строки
"""
from collections import Counter
from binarytree import build, Node
import math  # для высоты бинарного дерева: math.ceil(len(a) / 2), можно обойтись без этого

def go(bin_tree, number, path=''):  # функция для прохождения по дереву и получения последовательности из 0, 1 для number
    if number == bin_tree.value:
        return(f'{path}')
    if number < bin_tree.value and bin_tree.left is not None:
        return go(bin_tree.left, number, path=f'{path}0')
    if number > bin_tree.value and bin_tree.right is not None:
        return go(bin_tree.right, number, path=f'{path}1')
    return f'символ отсутствует'

print('Кодирование строки "good mood here!" по алгоритму Хаффмана')
a = Counter('good mood here!')
list_ = []  # коллекция с листьями будущего дерева, расположенными в порядке возрастания частоты
i = 0

for i in range(len(a)):
    for char, freq in Counter(a).items():  # строим очередь с помощью цикла
        if freq == i:
         list_.append((freq, char))
    i+=1
print('последовательность букв в порядке возрастания частоты', list_)
print("замена букв символами: 'g'=11, 'm'=9, 'h'=7, 'r'=5, '!'=13, 'd'=15, ' '=3, 'e'=17, 'o'=1")
#print('Высота бинарного дерева равна ', math.ceil(len(a) / 2))
""" 
введите строку: good mood here!
Counter({'o': 4, 'd': 2, ' ': 2, 'e': 2, 'g': 1, 'm': 1, 'h': 1, 'r': 1, '!': 1})
9
[(1, 'g'), (1, 'm'), (1, 'h'), (1, 'r'), (1, '!'), (2, 'd'), (2, ' '), (2, 'e'), (4, 'o')]
Высота бинарного дерева равна  5

как автоматизировать расстановку букв по дереву - не додумалась
[(1, 11, 'g'), (1, 9, 'm'), (1, 7, 'h'), (1, 5, 'r'), (1, 13, '!'), (2, 15, 'd'), (2, 3, ' '), (2, 17, 'e'), (4, 1, 'o')]
где должна быть какая буква - второй индекс элемента массива
бинарное поисковое дерево составляла вручную (не сделано главное в ПЗ)
"""
# строим дерево по алгоритму Хаффмана для кодирования букв в фразе
root = Node(8)
root.left = Node(2)
root.right = Node(16)
root.left.left = Node(1)
root.right.right = Node(17)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.right.left = Node(14)
root.right.left.right = Node(15)
root.right.left.left = Node(12)
root.right.left.left.right = Node(13)
root.left.right.right = Node(6)
root.left.right.right.left = Node(5)
root.left.right.right.right = Node(7)
root.right.left.left.left = Node(10)
root.right.left.left.left.left = Node(9)
root.right.left.left.left.right = Node(11)
print(root)  # наглядность
"""
# строим дерево с помощью build
values = [8, 2, 16, 1, 4, 14, 17, None, None, 3, 6, 12, 15, None, None, None, None, None, None, None, None, 5, 7, 10, 13, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 9, 11]
tree_ = build(values)
print(tree_)  # выводим на экран для наглядности
"""
# шагая по дереву с помощью go(), получаем словарь с кодировкой для букв: dict_ и раскодированием символов: inv_dict
dict_ = dict(
    zip(['o', ' ', 'r', 'h', 'm', 'g', '!', 'd', 'e'], [go(root, 1), go(root, 3), go(root, 5), go(root, 7),
                                                        go(root, 9), go(root, 11), go(root, 15), go(root, 13),
                                                        go(root, 17)]))
#print('кодировка букв: ', dict_)
inv_dict = {value: key for key, value in dict_.items()}
#print('раскодирование символов: ', inv_dict)

decoded_list = []  # закодированная строка: 10001 00 00 1001 010 10000 00 00 1001 010 0111 11 0110 11 101
encoded_phrase = []  # строка: good mood here!

phrase = 'good mood here!'

for i, char in enumerate(phrase):
    value = dict_[char]
    decoded_list.append(value)
print('закодированная фраза: ', decoded_list)

for char in decoded_list:
    value = inv_dict[char]
    encoded_phrase.append(value)
print('раскодированная строка: ', encoded_phrase)
