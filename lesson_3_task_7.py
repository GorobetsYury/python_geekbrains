# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0]
min_index = 0
ex_min_ = None
ex_min_index = None

for i in range(SIZE):       # поиск мин. значения
    if array[i] <= min_:
        min_ = array[i]
        min_index = i
print('Мин. значение в массиве : array[{}] = {}'.format(min_index, min_))

if min_ == array[0]:        # первоначальное определение ex_min_ для будущих вычислений
    ex_min_ = array[1]
else:
    ex_min_ = array[0]

count = 0                   # опредление ex_min_ исходя из условия повторения min_ в массиве
for i in range(SIZE):
    if array[i] == min_:
        count += 1
if count > 1:
    ex_min_ = min_
    print('Минимальное число повторяется {} раз/-а'.format(count))
elif count == 1:
    for i in range(SIZE):
        if array[i] == min_:
            continue
        if array[i] < ex_min_:
            ex_min_ = array[i]
            ex_min_index = i
    print('Пред мин. значение в массиве : array[{}] = {}'.format(ex_min_index, ex_min_))



