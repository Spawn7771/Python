# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного,
# игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать
##  “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.

import random

list_bolshe=[100]
list_menshe=[1]
m=0
b=0
i=0

number = random.randint(1, 100)
#print(number)

while True:
    print(number)
    usr_check = input()
    if usr_check == '=':
        print("Победа")
        break
    elif usr_check == '>':
        print("Загаданное число больше")
        if i==0:
            list_menshe.append(number)
            i += 1
            m += 1
        else:
            number = random.randint(list_menshe[m],list_bolshe[b])
            list_menshe.append(number)
            while list_menshe[m] == list_bolshe[b]:
                del list_menshe[-1]
                m -= 1
                number = random.randint(list_menshe[m], list_bolshe[b])
                list_menshe.append(number)
    elif usr_check == '<':
        print("Загаданное число меньше")
        if i==0:
            list_bolshe.append(number)
            b += 1
            i += 1
        else:
            number = random.randint(list_menshe[m], list_bolshe[b])
            list_bolshe.append(number)
            while list_menshe[m] == list_bolshe[b]:
                del list_bolshe[m]
                b -= 1
                number = random.randint(list_menshe[m], list_bolshe[b])
                list_bolshe.append(number)
    else:
        print("Вы ввели неправильный символ, разрешены только >,<,=")
    #print(number)