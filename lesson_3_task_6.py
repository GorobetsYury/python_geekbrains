# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# Пожалуй рискну и возьму за основу решение задачи №3 =)

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

sum_ = 0
if max_index < min_index:
    min_index, max_index = max_index, min_index
for i in range(min_index + 1, max_index):
    sum_ = sum_ + array[i]

print(array)
print('Сумма элементов между мин. элементом и макс. элементом равна - {}'.format(sum_))
