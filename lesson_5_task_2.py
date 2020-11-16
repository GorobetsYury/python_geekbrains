from collections import deque

# Задаю два вспомогательных словаря
my_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

help_dict = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

array_1 = deque(input('Введите первое число: '))
array_2 = deque(input('Введите второе число: '))
sum_ = deque()

# Выравниваю массивы
if len(array_1) < len(array_2):
    while len(array_1) != len(array_2):
        array_1.appendleft('0')
elif len(array_1) > len(array_2):
    while len(array_2) != len(array_1):
        array_2.appendleft('0')

# Делаю запас на случай, если сумма будет больше на порядок (например ABCDEF + ABCDEF)
array_1.appendleft('0')
array_2.appendleft('0')

add = 0 # В эту переменную записываю дополнительный "десяток", и обнуляю её при необходимости
for _ in reversed(range(len(array_1))):
    summary = my_dict[array_1[_]] + my_dict[array_2[_]] + add
    if summary <= my_dict['9']: # обычный случай
        sum_.appendleft(summary)
        add = 0
    elif 10 <= summary <= 15: # шестнадцатеричный случай, когда нужны буквы
        sum_.appendleft(help_dict[summary])
        add = 0
    elif summary == 16: # случай, когда пишем '0' и запоминаем +1 на следующий подсчет
        x = '0'
        sum_.appendleft(my_dict[x])
        add = 1
    elif summary > 16: # случай, когда записываем в результат не цифру > 0 и запоминаем +1 на следующий подсчет
        x = summary - 16
        if x <= my_dict['9']:
            x = str(x)
            sum_.appendleft(my_dict[x])
        elif 10 <= x <= 15:
            sum_.appendleft(help_dict[x])
        add = 1

print('Сумма {}'.format(sum_))



