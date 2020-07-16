name = input ('Vvedite Imya: ')
surname = input ('Vvedite Familiu: ')
age = int(input('Skolko vam let: '))
ves = int(input('Vvedite vash ves: '))
good = 'Horoshee sostoyanie'
soso = 'Sleduet zanyatsa soboy'
bad = 'sleduet obratitsa k vrachy'


if age > 40  and ((ves < 50) or (ves > 120)):
    print (name, end=' ')
    print(surname, end=', ')
    print(age, end=' ')
    print('god', end=', ')
    print('ves', end=' ')
    print(ves, end=' - ')
    print(bad)
    #print (name, surname ', ', age ' god', 'ves ' ves ' - ' bad)
elif age > 30  and ((ves < 50) or (ves > 120)):
    print(name, end=' ')
    print(surname, end=', ')
    print(age, end=' ')
    print('god', end=', ')
    print('ves', end=' ')
    print(ves, end=' - ')
    print(soso)
    #print (name"", surname", ", age" god", "ves "ves" - "soso)
elif age < 30  and ((ves > 50) and (ves < 120)):
    print(name, end=' ')
    print(surname, end=', ')
    print(age, end=' ')
    print('god', end=', ')
    print('ves', end=' ')
    print(ves, end=' - ')
    print(good)
    #print (name"", surname", ", age" god", "ves "ves" - "good)
else:
    print ('Sootnoshenie vashego vesa i vozrasta ne podpadaet ni pod odin iz kriteriev ozenki i trebuet bollee detalnogo rassmotrenia, izvinite')