# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# Вариант №2. Ваш вариант =) Правда и тут и в моем варианте по одному циклу.
import timeit
import cProfile

def dean_func(n):
    item = 1
    sum_ = 0
    for _ in range(n):
        sum_ += item
        item /= -2
    return sum_

print(timeit.timeit('dean_func(10)', number=100, globals=globals())) # 0.0003014
print(timeit.timeit('dean_func(20)', number=100, globals=globals())) # 0.0004815
print(timeit.timeit('dean_func(40)', number=100, globals=globals())) # 0.00087889
print(timeit.timeit('dean_func(80)', number=100, globals=globals())) # 0.0015982
print(timeit.timeit('dean_func(160)', number=100, globals=globals())) # 0.0028019
print(timeit.timeit('dean_func(320)', number=100, globals=globals())) # 0.01025949
print(timeit.timeit('dean_func(640)', number=100, globals=globals())) # 0.0082409
print(timeit.timeit('dean_func(1280)', number=100, globals=globals())) # 0.0216538
print(timeit.timeit('dean_func(2520)', number=100, globals=globals())) # 0.03865579
# График сильно штормило на 4-х точках. Решил взять побольше.
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing
# Вывод: бывает, что какая-то из точек выбивается из общей картины. Но в целом, если проэкстрапалировать график,
# взяв еще хотя бы точек 20, то можно сказать, что график имеет линейную зависимость.

cProfile.run('dean_func(1000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.2.py:6(dean_func)
cProfile.run('dean_func(2000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.2.py:6(dean_func)
cProfile.run('dean_func(3000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.2.py:6(dean_func)

# Вывод: неудачная функция для изучения через cProfile =(