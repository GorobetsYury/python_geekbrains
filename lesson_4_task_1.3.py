# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# Вариант №3. Ваш вариант через геометрическую прогрессию
import timeit
import cProfile

def geo_prog_func(n):
    sum_ = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return sum_

print(timeit.timeit('geo_prog_func(10)', number=100, globals=globals())) # 0.00017759
print(timeit.timeit('geo_prog_func(20)', number=100, globals=globals())) # 0.00010429
print(timeit.timeit('geo_prog_func(40)', number=100, globals=globals())) # 9.68e-05
print(timeit.timeit('geo_prog_func(80)', number=100, globals=globals())) # 9.45e-05
# Вывод: это бесконечно убывающая линия (сначала подумал, что похоже на гиперболу).
# Ссылка на график: https://drive.google.com/drive/folders/1Nl2dfV7U_xoELL5FCCL_Ev1UAAY_3oTP?usp=sharing
# Чем больше n, тем быстрее фукнция отработает.
# Это видно как из результатов, так и из графика

cProfile.run('geo_prog_func(1000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
#  1    0.000    0.000    0.000    0.000 lesson_4_task_1.3.py:6(geo_prog_func)
cProfile.run('geo_prog_func(2000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
#  1    0.000    0.000    0.000    0.000 lesson_4_task_1.3.py:6(geo_prog_func)
cProfile.run('geo_prog_func(3000)') # функция проста. cProfile не видит слабых мест. Всё по нулям
#  1    0.000    0.000    0.000    0.000 lesson_4_task_1.3.py:6(geo_prog_func)

# Вывод: неудачная функция для изучения через cProfile =(