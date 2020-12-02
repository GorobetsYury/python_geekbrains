# 64-разрядная ОС / Python 3.9.0
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import sys
# Способ №2 # Решил разнообразить решение и взял кортеж (64 байта), но не список (80 байт),
# пришлось завести переменные для подсчета и представить вводимое число в качестве строки.
number = input("Введите целое трёхзначное число: ")
number = tuple(number)
sum_ = 0
mult_ = 1

for i in number:
    sum_ += int(i)
    mult_ *= int(i)

print(f"Сумма цифр введённого Вами числа - {sum_}")
print(f"Произведение цифр введённого Вами числа - {mult_}")

def show(x):    # Упрощенная функция для подсчета суммы элементов массива count (не универальная)
    result = 0
    if hasattr(x, '__iter__'):
        result += sys.getsizeof(x)
        for item in x:
            if type(item) is str or int:
                result += sys.getsizeof(item)
    if type(x) is int:
        result += sys.getsizeof(x)
    return result

count = [number, sum_, mult_]
CONSTANT = 28 # Не придумал, как по иному учесть две переменные i на выходе из цикла for, когда я производил подсчет
# суммы и произведения.
total = CONSTANT * 2 # Т.к. одну переменную я суммирую, а вторую умножаю, я думаю, что нужно брать их в двойном кол-ве.
for i in count:
    total += show(i)

print(f'Сумма по всем объектам {total}')
# Сумма равна 326.
# Пример:
# Введите целое трёхзначное число: 123
# Сумма цифр введённого Вами числа - 6
# Произведение цифр введённого Вами числа - 6
# type(x)=<class 'tuple'>, sys.getsizeof(x)=64, x=('1', '2', '3') - размер отдельно кортежа number
# type(x)=<class 'str'>, sys.getsizeof(x)=50, x='1' - размер элемента кортежа
# type(x)=<class 'str'>, sys.getsizeof(x)=50, x='2' - размер элемента кортежа
# type(x)=<class 'str'>, sys.getsizeof(x)=50, x='3' - размер элемента кортежа
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=6  - размер элемента sum_
# type(x)=<class 'int'>, sys.getsizeof(x)=28, x=6  - размер элемента mult_
# и еще два раза по 28 за две переменные i в цикле
# Цифры сходятся
