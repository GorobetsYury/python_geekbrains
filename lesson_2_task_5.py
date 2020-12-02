# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://drive.google.com/file/d/1qY6_h5m474pSxlpz4_TJtYvFuesRXp19/view?usp=sharing

n = int(input('Введите любое натуральное число n : '))

def func(n):
    if n == 1:
        return 1
    if n > 1:
        return n + func(n-1)

part_1 = func(n)
part_2 = n*(n+1)/2

if part_1 == part_2:
    print('Равенство верно!')
else:
    print('Равенство неверно.')