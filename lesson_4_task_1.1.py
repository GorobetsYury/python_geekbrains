# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# Вариант №1. Мой оригинальный, который сдавал на ДЗ
import timeit
import cProfile

def my_func(n):
    i = 1
    sum_ = 0
    first_value = 1
    while i <= n:
        sum_ = sum_ + first_value
        first_value = first_value * (-0.5)
        i += 1
    else:
        return sum_

print(timeit.timeit('my_func(10)', number=100, globals=globals())) # 0.00013399999999999523
print(timeit.timeit('my_func(20)', number=100, globals=globals())) # 0.00023510000000000197
print(timeit.timeit('my_func(40)', number=100, globals=globals())) # 0.0004452000000000067
print(timeit.timeit('my_func(80)', number=100, globals=globals())) # 0.0008721999999999897
# Вывод: зависимость линейная
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing

cProfile.run('my_func(1000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.1.py:6(my_func)
cProfile.run('my_func(2000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.1.py:6(my_func)
cProfile.run('my_func(3000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
# 1    0.000    0.000    0.000    0.000 lesson_4_task_1.1.py:6(my_func)

# Вывод: неудачная функция для изучения через cProfile =(