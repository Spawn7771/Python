# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”. Если компьютер назвал число меньше загаданного,
# игрок должен выбрать “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать
##  “загаданное число меньше”. Игра продолжается до тех пор пока компьютер не отгадает число.

low = 1
high = 100
while True:
    number = (low+high)//2
    is_right = input(f'Ваше число:{number}?(=, >, <)')
    if is_right == '=':
        print('Победа')
        break
    elif is_right=='>':
        low = number + 1
    elif is_right=='<':
        high = number - 1
    else:
        print("Вы ввели неправильный символ, разрешены только >,<,=")