# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1qY6_h5m474pSxlpz4_TJtYvFuesRXp19/view?usp=sharing

number = input('Введите натуральное число: ')
even = 0
odd = 0
for i in number:
    i = int(i)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print('Нечётных цифр - {}'.format(odd))
print('Чётных цифр - {}'.format(even))
