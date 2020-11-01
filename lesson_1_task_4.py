# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1pWktHKV66QacajrB8EphgSu3fawntSR0/view?usp=sharing

letter_1 = input("Введите первую букву от 'a' до 'z': ")
letter_2 = input("Введите вторую букву от 'a' до 'z': ")

letters_between = ord(letter_2) - ord(letter_1) - 1
number_in_raw_1 = ord(letter_1) - 96
number_in_raw_2 = ord(letter_2) - 96

print("Буква '{}' является {} буквой в алфавите".format(letter_1, number_in_raw_1))
print("Буква '{}' является {} буквой в алфавите".format(letter_2, number_in_raw_2))
print("Между введенными буквами расположено ещё {} букв/-ы".format(letters_between))
