# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/1pWktHKV66QacajrB8EphgSu3fawntSR0/view?usp=sharing

letter_number = int(input("Введите алфавитный номер той буквы, которая Вас интересует: "))
letter = chr(letter_number + 96)

print("Под номером {} в алфавите расположена буква '{}'".format(letter_number, letter))
