# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#  При равенстве повторов показывает то число, у которого индекс меньше
count = 0
max_count = 0
number = None

for i in array:
    for j in array:
        if i == j:
            count += 1
    if count >= max_count:
        max_count = count
        number = i
    count = 0
if max_count == 1:
    print('Нет повторяющихся чисел.')
elif max_count != 1:
    print('Наиболее повторяющееся число в массиве - {}'.format(number))
print(array)






