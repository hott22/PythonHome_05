# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import re

file_path = 'D:/torrentfiles/mix.py'
# print(re.split("[.]", file_path))
# print(file_path.split('.'))


def my_func(path: str) -> tuple[str, str, str]:
    *_, b, c = re.split('/|[.]', path)
    my_tuple = (path, b, c,)
    return my_tuple


# print(my_func(file_path))

#  Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

name_list = ['Alex', 'Mary']
bet_list = [2000, 3000]
proc_list = ['10.25%', '11.6%']


gen_ = {name_list[item]: bet_list[item] * float(proc_list[item][:-1]) / 100 for item in range(len(name_list))}
# print(gen_)


# Создайте функцию генератор чисел Фибоначчи


def gen_fibb(number: int):
    fib1 = fib2 = 1
    if number == 1:
        yield fib2
    else:
        for i in range(number):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib2


print(*gen_fibb(6))
