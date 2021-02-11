# ПЗ2, задание 4 (Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.)
# решение преподавателя
# (интерпретированное, чтобы можно было анализировать с помощью timeit и cProfile)

import timeit
import cProfile

def summa_1(num):
    item = 1
    summa_1 = 0
    for _ in range(num):
        summa_1 += item
        item /= -2      # item *= -0.5
    return summa_1

# вариант с геометрической прогрессией
def summa_2(num):
    return 1 * (1 - (-0.5) ** num) / (1 - (-0.5))

# вариант с рекурсией
def sum_recursive(num, start=1.0, step=-0.5):
    if num == 1:
        return start
    if num > 55:
        return 2/3
    return start + sum_recursive(num - 1, start * step)

print(timeit.timeit('summa_1(10)', number = 100, globals=globals()))  # 0.00012770000000000142
print(timeit.timeit('summa_1(100)', number = 100, globals=globals()))  # 0.0008657(9)
print(timeit.timeit('summa_1(1000)', number = 100, globals=globals()))  # 0.008912(9)

cProfile.run('summa_1(10_000)')
cProfile.run('summa_1(100_000)')
cProfile.run('summa_1(1_000_000)')

"""
4 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 hw4_tsk1.py:9(summa_1)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 hw4_tsk1.py:9(summa_1)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.101 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.101    0.101 <string>:1(<module>)
        1    0.101    0.101    0.101    0.101 hw4_tsk1.py:9(summa_1)
        1    0.000    0.000    0.101    0.101 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

print(timeit.timeit('summa_2(10)', number = 100, globals=globals()))  # 0.0000640(9)
print(timeit.timeit('summa_2(100)', number = 100, globals=globals()))  # 0.00004320000000000018
print(timeit.timeit('summa_2(1000)', number = 100, globals=globals()))  # 0.000045(9)

cProfile.run('summa_2(10_000)')
cProfile.run('summa_2(100_000)')
cProfile.run('summa_2(1_000_000)')

"""
вызов только для 1_000_000, остальные значения аналогичные
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1.py:18(summa_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

print(timeit.timeit('sum_recursive(10)', number = 100, globals=globals()))  # 0.0004496000000000014
print(timeit.timeit('sum_recursive(100)', number = 100, globals=globals()))  # 0.00003200000000000425
print(timeit.timeit('sum_recursive(1000)', number = 100, globals=globals()))  # 0.0000288(9)

cProfile.run('sum_recursive(10_000)')
cProfile.run('sum_recursive(100_000)')
cProfile.run('sum_recursive(1_000_000)')

"""
вызов только для 1_000_000, остальные значения аналогичные
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1.py:22(sum_recursive)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

для последнего вызова cProfile(1_000_000) - цифр нет, анализировать с помощью cProfile нечего?
это происходит оттого, что начиная с 55-го члена последовательности 
сумма равна фиксированному значению?
это говорит о том, что код хорош? (если всё по нулям и функция sum_recursive отрабатывает без ошибок)
или я неправильно понимаю происходящее вообще?
"""
# общий вывод: самое времязатратное решение - с рекурсией.