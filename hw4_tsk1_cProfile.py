# ПЗ3, задача4 (Определить, какое число в массиве встречается чаще всего)
# поиск слабых мест в коде (cProfile)
import random
import cProfile

def array_maker(size):
    return [random.randint(0, 100) for _ in range(size)]

# вариант 1 с обращением по индексу и вложенными циклами
def func_max_input1(array):
    spam = array[0]  # предполагаемое число, которое встречается в массиве чаще всего
    max_frequency = 1
    for i in range(len(array)):
        frequency = 1
        for f in range(i + 1, len(array)):
            if array[i] == array[f]:
                frequency += 1
        if frequency > max_frequency:
            max_frequency = frequency
            spam = array[i]

    return max_frequency

# ваниант 2 со словарём
def dict_counter_maker(array):
    dict_counter = {}
    for item in array:
        if item in dict_counter:
            dict_counter[item] += 1
        else:
            dict_counter[item] = 1
    return dict_counter

def frequency(dict_counter):
    frequency = 1
    num = None
    for item in dict_counter:
        if dict_counter[item] > frequency:
            frequency = dict_counter[item]
            num = item
    return frequency

def main1(size):
    array = array_maker(size)
    freq_max = func_max_input1(array)

def main2(size):
    array = array_maker(size)
    dict_counter = dict_counter_maker(array)
    freq_max = frequency(dict_counter)

cProfile.run('main1(10)')
cProfile.run('main1(100)')
cProfile.run('main1(1_000)')

"""
   68 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:13(func_max_input1)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:46(main1)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:9(array_maker)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
       10    0.000    0.000    0.000    0.000 random.py:218(randint)
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         641 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:13(func_max_input1)
        1    0.000    0.000    0.001    0.001 hw4_tsk1_cProfile.py:46(main1)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:9(array_maker)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      133    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


         6285 function calls in 0.052 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.052    0.052 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 hw4_tsk1_cProfile.py:10(<listcomp>)
        1    0.049    0.049    0.050    0.050 hw4_tsk1_cProfile.py:13(func_max_input1)
        1    0.000    0.000    0.052    0.052 hw4_tsk1_cProfile.py:46(main1)
        1    0.000    0.000    0.002    0.002 hw4_tsk1_cProfile.py:9(array_maker)
     1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1277    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"КРУТО", если функции main1/2 написаны неверно - смысл анализируемого отсутствует. в правильности написания main не уверена. 
вывод:
func_max_input1 - слабое место в коде (2 вложенных цикла, время выполнения увеличивается по закономерности O(size**2)
графически - по параболе)
следует поискать более оптимальное решение - без вложенных циклов
"""

cProfile.run('main2(10)')
cProfile.run('main2(100)')
cProfile.run('main2(1_000)')

""" 

         60 function calls in 0.000 seconds  -- 60 вызовов за 0 сек

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:16(frequency)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:26(main2) 
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:4(array_maker)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:5(<listcomp>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:7(dict_counter_maker)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)  
       10    0.000    0.000    0.000    0.000 random.py:218(randint)    
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}  
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

-- у интересующих самостоятельно написанных функций (dict_counter_maker, array_maker, frequency, main2) 
время маленькое, вызываются они по разу - это хорошо
-- встроенные функции randrange, randint, _randbelow вызываются часто,
но они встроенные (из коробки), это не так накладно/допустимо/этим можно пренебречь
-- не понимаю про method вообще, но вызываются часто, без затрат времени пока


         537 function calls in 0.000 seconds  
         
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:16(frequency)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:26(main2)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:4(array_maker)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:5(<listcomp>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:7(dict_counter_maker)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

-- увеличивается кол-во вызавов 
(с 60 до 537, размер увеличили с 10 до 100 - 
почти пропорционально размеру увеличивается кол-во вызовов функций)

         5294 function calls in 0.002 seconds 
         
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:16(frequency)
        1    0.000    0.000    0.002    0.002 hw4_tsk1_cProfile.py:26(main2)
        1    0.000    0.000    0.002    0.002 hw4_tsk1_cProfile.py:4(array_maker)
        1    0.000    0.000    0.002    0.002 hw4_tsk1_cProfile.py:5(<listcomp>)
        1    0.000    0.000    0.000    0.000 hw4_tsk1_cProfile.py:7(dict_counter_maker)
     1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1286    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
     
-- увеличивается кол-во вызавов (с 60 до 5294, размер увеличили с 10 до 1000, аналогично второму вызову cProfile)
--  появляется время вызова

общий вывод:
1) самые часто вызываемые функции: randrange, randint, _randbelow 
(на них тратится и время, но они встроенные - наверное, не так опасно для кода)
2) написанные функции dict_counter_maker и frequency почти не затрачивают на своё выполнение время - это хорошо для кода.
3) <listcomp> - не понимаю, что это - компилляция списка? - на это тратится время
слабое место в коде - создание рандомного массива - но обойти его нельзя.
решение со словарём - лучшее из рассмотренных.
"""
