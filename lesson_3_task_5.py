# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
negative_array = []

for num in array:
    if num < 0:
        negative_array.append(num)
if negative_array == []:
    print('В массиве нет отрицательных чисел.')
else:
    result = negative_array[0]
    for num in negative_array:
        if num > result:
            result = num

    for i in range(len(array)):
        if array[i] == result:
            print('array[{}] = {}'.format(i, result))
    print(array)

# Хотел решить в один цикл - с ходу получилось найти только "минимальный" элемент массива.
# result = 0
# result_index = None
# for i in range(len(array)):
#     if array[i] < result:
#         result = array[i]
#         result_index = i
# if result == 0:
#     print('В массиве нет отрицательных чисел.')
# else:
#     print('array[{}] = {}'.format(result_index, result))
# print(array)
