def max_chislo(chislo1, chislo2, chislo3):
    return max(chislo1, chislo2, chislo3)

chislo1=int(input("Введите первое число: "))
chislo2=int(input("Введите второе число: "))
chislo3=int(input("Введите третье число: "))

result=max_chislo(chislo1, chislo2, chislo3)

text='Максимальное число {}'.format(result)

print(str(text))
