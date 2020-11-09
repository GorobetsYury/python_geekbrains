# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_number = array[0]
max_number = array[0]
min_index = 0
max_index = 0

for i in range(SIZE):
    if array[i] < min_number:
        min_index = i
        min_number = array[i]
    elif array[i] >= max_number:
        max_index = i
        max_number = array[i]
array[min_index], array[max_index] = array[max_index], array[min_index]

print('Индекс мин. элемента: {}'.format(min_index))
print('Индекс макс. элемента: {}'.format(max_index))
print(array)
