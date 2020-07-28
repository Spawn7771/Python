# Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел (если число #отрицательное) и
# возвращает результат (желательно применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
#Например:
#old_list = [1, -3, 4]
#result = [1, -3, 2]

import math

def my_sqrt(input_list):

    if input_list:
        lst = input_list
        lst2 = lst[:]
        l=len(lst)
        fin = []

        for i in range(l):
            #сразу скажу что функцией math.trunc я отсекаю дробную часть для наглядности (как написано в задании), так что не нужно считать это ошибкой
            fin.append(math.trunc(math.sqrt(lst2[i]))) if lst2[i] >= 0 else fin.append(lst2[i])
        return fin


print(my_sqrt([1,8,-4,64,121,-7,25,-11,9000, 625, -56, -8967, 7921,48,15,11,-555,-2387]))