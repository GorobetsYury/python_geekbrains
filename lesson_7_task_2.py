# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Данный разбор кода я посмотрел в интернете на одном и образовательных видео.
# Сначала поумал, что понял, потом ооочень долго пытался понять рекурсивный вызов функции, в этом помог отладчик.
# При помощи отладчика удалось понять, как я сначала отсортировал левую часть при помощи второй функции, а потом
# правую. Всё равно есть большой осадок от того, что списал решение. Из плюсов - научился работать с отладчиком и
# понял, как работает алгоритм. Ушло часа 2.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0 and len(right) == 0:
        result += left
    if len(right) > 0 and len(left) == 0:
        result += right
    return result


print(f'Исходный массив \n {array}')
print(f'Отсортированный массив \n {merge_sort(array)}')
