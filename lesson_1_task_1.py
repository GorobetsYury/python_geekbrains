# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1pWktHKV66QacajrB8EphgSu3fawntSR0/view?usp=sharing

number = int(input("Введите целое трёхзначное число: "))
num_1 = number%10
num_2 = (number%100)//10
num_3 = number//100
result_sum = num_1+num_2+num_3
result_mult = num_1*num_2*num_3
print("Сумма цифр введённого Вами числа - {}".format(result_sum))
print("Произведение цифр введённого Вами числа - {}".format(result_mult))
