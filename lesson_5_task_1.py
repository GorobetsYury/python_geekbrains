from collections import defaultdict  # Используется в строчках 7 - 10
from collections import deque  # Используется со строчки 22

result_dict = {}  # результирующий словарь, ключ - имя компании, значение - прибыль компании на 4 квартала
count_company = int(
    input('Введите количество компаний: '))  # вносим данные по компаниям (имя, прибыль по кварталам) с клавиатуры
for i in range(1, count_company + 1):
    name = input('Введите название {} компании: '.format(i))
    company_dict = defaultdict(list)
    for _ in range(1, 5):
        company_profit = int(input('Введите прибыль за {}-й квартал: '.format(_)))
        company_dict[name].append(company_profit)
    total_company_profit = sum(company_dict[name])
    result_dict[name] = total_company_profit # в итоге получаем словарь { "имя компании": "суммарная прибыль за 4 квартала" }

sum_ = 0  # подсчет средней прибыли по всем компаниям
for val in result_dict.values():
    sum_ += val
middle_profit = sum_ / count_company
print('Средний доход по компаниям равен - {}'.format(middle_profit))

profit_companies = deque()
no_profit_companies = deque()
zero_companies = deque()

for key in result_dict.keys():  # разделение компаний по прибыльности.
    if result_dict[key] < middle_profit:
        no_profit_companies.appendleft(key)
    elif result_dict[key] > middle_profit:
        profit_companies.appendleft(key)
    elif result_dict[key] == middle_profit:
        zero_companies.appendleft(key)
print('Прибыльные компании - {}'.format(profit_companies))  # оглашение результатов
print('Убыточные компании - {}'.format(no_profit_companies))
print('Вышедшие в 0 компании - {}'.format(zero_companies))

#  Использовал deque() + appendleft специально, т.к. тренируем библиотеки, а у appendleft асимптотика О(1), хотя
#  можно было бы в данном случае использовать и простой list + append. Я это понимаю.

# Это если выводить не отдельно списком сначала прибыльные, а замет убыточные, а по порядку.
# for key in result_dict.keys():
#     if result_dict[key] < middle_profit:
#         print('Компания {} убыточна'.format(key))
#     elif result_dict[key] > middle_profit:
#         print('Компания {} прибыльна'.format(key))
#     else:
#         print('Компания {} вышла в 0'.format(key))
