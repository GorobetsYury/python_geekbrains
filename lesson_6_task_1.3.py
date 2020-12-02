# 64-разрядная ОС / Python 3.9.0
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import sys
from collections import defaultdict
# Способ №3 # тут специально решил нагородить немыслимое для сложности вычисления данных.
# С моим подходом к подсчету я стал заложником извращенности решения. Тонкость заключалась в том, что я решал через
# defaultdict(list), и получилось так, что мне нужно было учесть, что каждый ключ в словаре- это еще и отдельный список,
# величину которого нужно было посчитать, не забыв при этов величину элемента в списке.
# Проверял себя по вашей чудо-функции. Цифры сходятся.
i = 1
new_number = defaultdict(list)
while i <= 3:
    number = int(input(f"Введите {i} цифру трёхзначного числа: "))
    new_number[i].append(number)
    i += 1

result_array = [] # Сюда собираю все значения цифр, чтобы потом взять сумму
mult_ = 1
for val in new_number.values():
    result_array.append(val[0])
    mult_ *= val[0]

sum_ = sum(result_array)
print(f"Сумма цифр введённого Вами числа - {sum_}")
print(f"Произведение цифр введённого Вами числа - {mult_}")

count = [i, new_number, result_array, mult_, sum_]
CONSTANT = 28 # Как и в прошлом задании решил сделать просто константу для подсчета переменной в конце цикла
total = CONSTANT * 2  # Т.к. два цикла, взял две константы.


def show(x):    # Функция для подсчета суммы элементов массива count (не универальная). Хотел написать "упрощенная",
    # но потом посмотрел на нее и в голос посмеялся. Зато оправдываю ваши слова "прокачиваем алгоритмическое мышление"=)
    result = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            result += sys.getsizeof(x)
            for key, value in x.items():
                result += sys.getsizeof(key)
                result += sys.getsizeof(value)
                if isinstance(value, list):
                    for i in value:
                        result += sys.getsizeof(i)
        elif isinstance(x, list):
            result += sys.getsizeof(x)
            for i in x:
                result += sys.getsizeof(i)
    elif isinstance(x, int):
        result += sys.getsizeof(x)
    return result

for _ in count:
    total += show(_)

print(f'Сумма по всем объектам {total}')
# Сумма равна 984.
# Пример:
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=4
# type(x)=<class 'collections.defaultdict'>, sys.getsizeof(x)=240, x=defaultdict(<class 'list'>, {1: [3], 2: [3], 3: [3]})
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=1
# type(x)=<class 'list'>, sys.getsizeof(x)=88, x=[3]
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=2
# type(x)=<class 'list'>, sys.getsizeof(x)=88, x=[3]
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'list'>, sys.getsizeof(x)=88, x=[3]
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'list'>, sys.getsizeof(x)=88, x=[3, 3, 3]
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=3
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=27
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=9
# и еще два раза по 28 за два цикла
# Цифры сходятся
