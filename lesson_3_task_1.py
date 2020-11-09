# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

start = 2
end = 9
while True:
    sum_ = 0
    if start > end:
        print('Конец')
        break
    elif start <= end:
        for item in range(2, 100):
            if item % start == 0:
                sum_ += 1
        print('В диапазоне от 2 до 99 есть {} чисел, кратных {}'.format(sum_, start))
    start += 1



