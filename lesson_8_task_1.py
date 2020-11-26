# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и
# строку целиком. Пример работы функции: func("papa") --> 6 ; func("sova") --> 9

import hashlib

stroke = input('Введите строку: ')
count_array = []


def mycount(str_):
    str_hash = hashlib.sha256(str_.encode('utf-8')).hexdigest()
    if len(str_)%2 == 0 and len(str_) == 2: # Это случай, если букв чётное количество, т.к. если этого не сделать,
        # то на следующем шаге рекурсии str_ = str_[1:-1] у меня два центральных символа строки не будут учтены и
        # хэши этих отдельных элементов, и их совместный хэш тоже
        a = hashlib.sha256(str_[0].encode('utf-8')).hexdigest()
        b = hashlib.sha256(str_[1].encode('utf-8')).hexdigest()
        c = hashlib.sha256((str_[0] + str_[1]) .encode('utf-8')).hexdigest()
        if a not in count_array:
            count_array.append(a)
        if b not in count_array:
            count_array.append(b)
        if c not in count_array:
            count_array.append(c)
        if str_hash in count_array:
            count_array.remove(str_hash)
        return f'Количество подстрок в слове "{stroke}" составляет {len(count_array)}'

    if len(str_)%2 != 0 and len(str_) == 1: # Это случай, если букв нечётное количество, и мы завершаем им обход строки
        a = hashlib.sha256(str_[0].encode('utf-8')).hexdigest()
        if a not in count_array:
            count_array.append(a)
        if str_hash in count_array:
            count_array.remove(str_hash)
        return f'Количество подстрок в слове "{stroke}" составляет {len(count_array)}'

    n = 0 # основной цикл, в котором я беру хэши подстрок помещаю в результирующий массив count_array
    while len(str_) > n:
        result = ''
        for i in range(n, len(str_)):
            result = (result + str_[i])
            hash_ = hashlib.sha256(result.encode('utf-8')).hexdigest()
            if hash_ not in count_array:
                count_array.append(hash_)
        n += 1
    else:
        str_ = str_[1:-1] # отсекаю строку, т.к. хэши двух крайних символов я учел предыдущем пробеге по строке
    return mycount(str_)


print(mycount(stroke))

# По факту, я просто открыл текстовый редактор, написал слово "окна" и начал думать, как решать.
# Начал мысленно бежать по слову и, дойдя до конца, отсекал первую букву:
# "окна" (n = 0)
# о, ок, окн, окна
# "кна" (n = 1)
# к, кн, кна
# "на" (n = 2)
# н, на
# "а" (n = 3)
# а
# Потом рекурсивно обрезаю слово по краям, пока не попаду в if по условию, где длина строки =2 или =1.



