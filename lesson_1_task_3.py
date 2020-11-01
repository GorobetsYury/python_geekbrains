# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# https://drive.google.com/file/d/1pWktHKV66QacajrB8EphgSu3fawntSR0/view?usp=sharing

import random
min_int = int(input("Введите целое число, которое будет являться нижней границей диапазона выборки: "))
max_int = int(input("Введите целое число, которое будет являться верхней границей диапазона выборки: "))
result_rand_int = random.randint(min_int,max_int)
print("Случайное число из указанного диапазона: {}".format(result_rand_int))

min_float = float(input("Введите вещественное число, которое будет являться нижней границей диапазона выборки: "))
max_float = float(input("Введите вещественное число, которое будет являться верхней границей диапазона выборки: "))
result_rand_float = random.uniform(min_float,max_float)
print("Случайное число из указанного диапазона: {}".format(result_rand_float))

import random
letter_1 = input("Введите первую букву из диапазона выборки: ")
letter_2 = input("Введите вторую букву из диапазона выборки: ")

start = ord(letter_1)
end = ord(letter_2)

result_rand_letter = random.randint(start,end)
result_rand_letter = chr(result_rand_letter)
print("Случайная буква из введенного диапазона: {}".format(result_rand_letter))