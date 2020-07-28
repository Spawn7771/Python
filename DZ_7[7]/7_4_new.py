def my_function(num):
    """
    Если число равно 13 - поднимает исключительную ситуацию ValueError
    если число > 100 или < 1 - поднимает исключительную ситуацию Exception
    возводит число в квадрат во всех остальных случаях
    """
    if num == 13:
        raise ValueError('Число 13')
    elif num > 100 or num < 1:
        raise Exception('Число меньше 1 или больше 100')
    else:
        return num**2

try:
    chislo = int(input('Введите целое число от 1 до 100: '))
    try:
        print(f'Квадрат числа равен: {my_function(chislo)}')
    except ValueError as exec:
        print(f'Число 13 не может быть возведено в квадрат, было вызвано исклбючение {ValueError}')
    except Exception as exec:
        print('Число должно быть от 1 до 100')
except:
    print('Вы ввели не число!')
finally:
    print('Программа завершена')