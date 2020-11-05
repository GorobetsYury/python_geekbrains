# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1qY6_h5m474pSxlpz4_TJtYvFuesRXp19/view?usp=sharing

n = int(input('Введите целое, натуральное число n: '))
i = 1
sum = 0
FIRST_VALUE = 1
while i <= n:
    sum = sum + FIRST_VALUE
    FIRST_VALUE = FIRST_VALUE * (-0.5)
    i += 1
else:
    print('Сумма "n" элементов последовательности "1, -0.5, 0.25, -0.125, …", где "n"={} равна {}'.format(n, sum))
