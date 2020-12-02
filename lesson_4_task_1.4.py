# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# Вариант №4. Мой вариант через рекурсию.
import timeit
import cProfile

def func_req(n):
    if n == 1:
        return 1
    if n > 1:
        return 1 - 0.5 * func_req(n - 1)

print(timeit.timeit('func_req(10)', number=100, globals=globals())) # 0.0002257
print(timeit.timeit('func_req(20)', number=100, globals=globals())) # 0.00042569
print(timeit.timeit('func_req(40)', number=100, globals=globals())) # 0.00091229
print(timeit.timeit('func_req(80)', number=100, globals=globals())) # 0.00223769
# Вывод: зависимость линейная
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing

cProfile.run('func_req(10)') # функция проста. cProfile не видит слабых мест. Вызов рекурсии - 10 раз. Всё по нулям
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #   10/1    0.000    0.000    0.000    0.000 lesson_4_task_1.4.py:6(func_req)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_req(100)') # функция проста. cProfile не видит слабых мест. Вызов рекурсии - 100 раз. Всё по нулям
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #  100/1    0.000    0.000    0.000    0.000 lesson_4_task_1.4.py:6(func_req)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_req(200)') # функция проста. cProfile не видит слабых мест. Вызов рекурсии - 200 раз.
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #  200/1    0.001    0.000    0.001    0.001 lesson_4_task_1.4.py:6(func_req)
   #      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: неудачная функция для изучения через cProfile =(
