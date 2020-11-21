# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

M = 5
SIZE = 2 * M + 1
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def coctail_sort(arr): # разборался, как работает. Это несомненно плюс. Подсмотрел код - это явный минус. Забыл,
    # как шагать по массиву в обратном направлении. Тихий ужас.
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr


def mediana_func(arr):
    middle = len(arr) // 2
    return arr[middle]


print(f'Массив на входе {array}')
print(f'Отсорт. массив шейкером {coctail_sort(array)}')
print(f'Медиана массива {mediana_func(array)}')
