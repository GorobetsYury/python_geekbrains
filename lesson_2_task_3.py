# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/1qY6_h5m474pSxlpz4_TJtYvFuesRXp19/view?usp=sharing

number = input('Введите число: ')
result = ''
for i in reversed(number):
    result += i
print('Ваше число наоборот - {}'.format(result))
