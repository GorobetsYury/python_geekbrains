# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = [[] for _ in range(5)]

for i in range(5):
    for j in range(3):
        result = int(input('Введите элемент матрицы [{}][{}]: '.format(i,j)))
        matrix[i].append(result)

for array in matrix:
    sum_ = 0
    for num in array:
        sum_ = sum_ + num
    array.append(sum_)

print(*matrix, sep='\n')
