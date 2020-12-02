# Написал свою функцию по поиску простых чилел. Как это вижу я. Она имеет квадратичную зависимость. Это плохо.
# Знаю, что можно как то сделать гораздо быстрее, через поиск корня из 'n', однако я не совсем понял это и
# решил не делать копи-паст из интернета, тем более так интереснее посмотреть насколько медленнее получится моё решение.
# Ведь в этом весь смак данного урока.
import timeit
import cProfile

def my_is_prime(num, n):
    sieve = [i for i in range(2, n + 1)]
    count = 0
    is_prime = []
    for i in sieve:
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            is_prime.append(i)
        count = 0
    return is_prime[num - 1]

print(timeit.timeit('my_is_prime(6,100)', number=100, globals=globals())) # 0.0659945
print(timeit.timeit('my_is_prime(12,200)', number=100, globals=globals())) # 0.1612968
print(timeit.timeit('my_is_prime(24,400)', number=100, globals=globals())) # 0.444451
print(timeit.timeit('my_is_prime(36,600)', number=100, globals=globals())) # 1.040192
print(timeit.timeit('my_is_prime(48,800)', number=100, globals=globals())) # 1.9136013
# Вывод: на графике получилась чистейшая ветвь параболы, устремленная вверх. Как будет видно далее, эта реализация
# алгоритма гораздо хуже, чем вторая, горадо более правильная реализаци.
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing

cProfile.run('my_is_prime(6,100)')
#      30 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:7(my_is_prime)
#     1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:8(<listcomp>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#    25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('my_is_prime(12,200)')
# 51 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 lesson_4_task_2.py:7(my_is_prime)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:8(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('my_is_prime(24,400)')
# 83 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 lesson_4_task_2.py:7(my_is_prime)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:8(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#        78    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('my_is_prime(36,600)')
# 114 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.021    0.021    0.021    0.021 lesson_4_task_2.py:7(my_is_prime)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:8(<listcomp>)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#       109    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('my_is_prime(48,800)')
# 144 function calls in 0.037 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.037    0.037 <string>:1(<module>)
#         1    0.037    0.037    0.037    0.037 lesson_4_task_2.py:7(my_is_prime)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:8(<listcomp>)
#         1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
#       139    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# У функции просто меняется время на обработку и количество append'ов, что логично. Работает не так быстро, как
# хотелось бы. Вина лежит, по большей части, на квадратичной зависимости и на несовершенном коде.

def sieve(num, n):
    is_prime = []
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            is_prime.append(sieve[i])
            while j < n:
                sieve[j] = 0
                j += i
    return is_prime[num - 1]

print(timeit.timeit('sieve(6,100)', number=100, globals=globals())) # 0.0049825
print(timeit.timeit('sieve(12,200)', number=100, globals=globals())) # 0.0100972
print(timeit.timeit('sieve(24,400)', number=100, globals=globals())) # 0.01117219
print(timeit.timeit('sieve(36,600)', number=100, globals=globals())) # 0.0237082
print(timeit.timeit('sieve(48,800)', number=100, globals=globals())) # 0.0297622
print(timeit.timeit('sieve(96,1600)', number=100, globals=globals())) # 0.07709
print(timeit.timeit('sieve(192,3200)', number=100, globals=globals())) # 0.14747539
# Вывод: функция отработала гораздо быстрее, чем моя функция. Думаю, что это линейная зависимость.
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing

cProfile.run('sieve(6,100)')
# 30 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:89(sieve)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:91(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(12,200)')
# 51 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:89(sieve)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:91(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(24,400)')
# 83 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:89(sieve)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:91(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        78    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(36,600)')
# 114 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:89(sieve)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:91(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       109    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(48,800)')
# 144 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:89(sieve)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:91(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       139    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: все по нулям. cProfile не видит за то зацепиться. Функция действительно быстрая.
