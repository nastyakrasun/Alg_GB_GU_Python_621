"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import timeit
import cProfile
# первый алгоритм
def sieve(num):
    array = []
    n = 10_000  # чтобы все программы были в относительно равных условиях, сделала ряд проверяемых чисел до 10_000
    array_sieved = [i for i in range(n)]
    array_sieved[1] = 0

    for i in range(2, n):
        if array_sieved[i] != 0:
            j = i + i
            while j < n:
                array_sieved[j] = 0
                j += i

    for i in array_sieved:
        if i != 0:
            array.append(i)
    return array[num-1]

#print(sieve(10))  # 29
#print(sieve(100))  # 541
#print(sieve(1000))  # 7919

# второй алгоритм: наивный перебор
#1 - моё решение
""" 
Проверка на простоту: 
перебирая числа k из диапазона от 2 до n−1, будем делить n на k с остатком. 
Если при каком-то k обнаружится нулевой остаток, значит, n делится на k нацело, и число n составное. 
Если же при делении обнаруживались только ненулевые остатки, значит, число простое; 
в этом случае выводим его на экран. 
Ясно, что, получив нулевой остаток (тем самым обнаружив, что n составное), 
следует отказаться от дальнейших проб на делимость.

Заметим, что все простые числа, за исключением двойки, нечётные. 
Если обработать особо случай n=2, то все последующие числа n можно перебирать с шагом 2. 
Это даст приблизительно двукратное увеличение производительности программы.
"""

def simple_by_number(num):
    n = 10_000  # ограниченное число простых чисел - выдаст ошибку при задании слишком большого num ВСЁ ВЕЗДЕ ПОРТИТ
    array_of_simple = [2]
    for k in range(3, n, 2):  # так как чётные числа >2 простые, исключим их из перебора
        for i in array_of_simple:
             if k % i == 0:  # если число делится нацело на простое, меньшее себя, - исключим его
                break
        else:  # число не чётное, не делится нацело ни на одно простое, меньшее себя, - оно само простое, в массив его
            array_of_simple.append(k)
    return array_of_simple[num-1]

#print(simple_by_number(10))  # 29
#print(simple_by_number(100))  # 541
#print(simple_by_number(1000))  # 7919

#2 подсмотренное решение (переделанное, понятое, анализируемое для понимания процесса упрощения алгоритма)
s = """ как анализировать без введения функции - не знаю. с введением функции ооочень долго проверяет 1_000_000 чисел
n = 1_000_000
array = [2]

for i in range(3, n+1, 2):
    #if (i > 10) and (i % 5 == 0):  # понятое, но сама бы так пока не написала
        #continue
    for j in array:
        if i % j == 0:
            break
        if j*j-1 > i:
            array.append(i)
            break
    else:
        array.append(i)

array[9]  # 29
"""
#print(array[99])  # 541
#print(array[999])  # 7919

def simple_by_number2(num):
    n = 10_000
    array = [2]
    for i in range(3, n + 1, 2):
        for j in array:
            if i % j == 0:
                break
            if j * j - 1 > i:
                array.append(i)
                break
        else:
            array.append(i)
    return array[num-1]

#print(simple_by_number2(10))  # 29
#print(simple_by_number2(100))  # 541
#print(simple_by_number2(1000))  # 7919
"""
# анализ timeit
print(timeit.timeit('sieve(10)', number = 100, globals=globals()))  # 0.6353988
print(timeit.timeit('sieve(100)', number = 100, globals=globals()))  # 0.6167549999999999
print(timeit.timeit('sieve(1000)', number = 100, globals=globals()))  # 0.5456561999999998

print(timeit.timeit('simple_by_number(10)', number=100, globals=globals()))  # 6.935060200000001
print(timeit.timeit('simple_by_number(100)', number = 100, globals=globals()))  # 6.7283227
print(timeit.timeit('simple_by_number(1000)', number = 100, globals=globals()))  # 6.836637199999998

# print(timeit.timeit(s, number = 100, globals=globals()))  # неудачная попытка анализа - fail
print(timeit.timeit('simple_by_number2(10)', number=100, globals=globals()))  # 0.8125764
print(timeit.timeit('simple_by_number2(100)', number=100, globals=globals()))  # 0.8287163000000001
print(timeit.timeit('simple_by_number2(1000)', number=100, globals=globals()))  # 0.8234608000000001

# вывод: быстрее всего работает алгоритм по решету Эратосфена, 
# медленнее всего - мой алгоритм 
# по поводу прикидки графика алгоритма: 
# в решете Эратосфена наблюдается уменьшение времени при увеличении номера искомого числа 
# (какая-то убывающая функция, возможно, прямая)
# в 2 других алгоритмах - скачкообразные значения (это не прямая, не ВЕТВЬ параболы, дальше не думается)
"""
# анализ cProfile - думаю, провожу не совсем верно (уместно) - на входящие в состав алгоритма функции не раскладывала
# НО ПРОВОЖУ
cProfile.run('sieve(10)')
cProfile.run('sieve(100)')
cProfile.run('sieve(1000)')
"""
1234 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.008    0.008    0.009    0.009 hw4_tsk2.py:15(sieve)
        1    0.001    0.001    0.001    0.001 hw4_tsk2.py:18(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1234 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.007    0.007    0.008    0.008 hw4_tsk2.py:15(sieve)
        1    0.001    0.001    0.001    0.001 hw4_tsk2.py:18(<listcomp>)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1234 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.009    0.009    0.010    0.010 hw4_tsk2.py:15(sieve)
        1    0.001    0.001    0.001    0.001 hw4_tsk2.py:18(<listcomp>)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
     1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

cProfile.run('simple_by_number(10)')
cProfile.run('simple_by_number(100)')
cProfile.run('simple_by_number(1000)')
""" 
1232 function calls in 0.074 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.073    0.073 <string>:1(<module>)
        1    0.073    0.073    0.073    0.073 hw4_tsk2.py:53(simple_by_number)
        1    0.000    0.000    0.074    0.074 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1232 function calls in 0.070 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.069    0.069 <string>:1(<module>)
        1    0.069    0.069    0.069    0.069 hw4_tsk2.py:53(simple_by_number)
        1    0.000    0.000    0.070    0.070 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1232 function calls in 0.072 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.072    0.072 <string>:1(<module>)
        1    0.072    0.072    0.072    0.072 hw4_tsk2.py:53(simple_by_number)
        1    0.000    0.000    0.072    0.072 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
"""

cProfile.run('simple_by_number2(10)')
cProfile.run('simple_by_number2(100)')
cProfile.run('simple_by_number2(1000)')
""" 
 1232 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.008    0.008    0.008    0.008 hw4_tsk2.py:90(simple_by_number2)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1232 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
        1    0.013    0.013    0.014    0.014 hw4_tsk2.py:90(simple_by_number2)
        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1232 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
        1    0.014    0.014    0.014    0.014 hw4_tsk2.py:90(simple_by_number2)
        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
     1228    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
# общий вывод по cProfile:
# алгоритм с решетом Эратосфена работает быстрее всего,
# хорошо отрабатывает алгоритм simple_by_number2 .
# то, для чего принимался в работу simple_by_number2,
# - разложение на входящие функции и анализ отрабатывания каждой из них - не делается.
# поэтому выяснить алгоритмически, почему так медленно работает алгоритм simple_by_number здесь сейчас нельзя.
# времени нет, но знаю, как делать (лишь бы входящие функции правильно задавать - в этом не уверена).
# append загоняли
