chislo = int(input('Vvedite chislo: '))
while (chislo <= 0) or (chislo >= 10):
        if (chislo <= 0):
            chislo = int (input('Vy vveli nepravilnoe, vvedite chislo bolshe '))
        else:
            chislo = int (input('Vy vveli nepravilnoe, vvedite chislo menshe '))

result = chislo ** 2
print (result)
