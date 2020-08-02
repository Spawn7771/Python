#Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
#name - строка полученная от пользователя,
#health = 100,
#damage = 50.
#Поэкспериментируйте с значениями урона и жизней по желанию.
#Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
#Функция в качестве аргумента будет принимать атакующего и атакуемого.
#В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.


def attack(player, enemy):

    zdorovie = player_dict['health']
    yron = enemy_dict['damage']
    res = zdorovie - yron
    player_dict['health'] = res
    return res


player= input("Введите имя атакуемого: ")
enemy =  input("Введите имя атакуещего: ")
zdor =  int(input("Введите кол-во здоровья атакуемого: "))
yr =  int(input("Введите урон атакуещего: "))

player_dict = {
    'name' : player,
    'health': zdor,
    'damage': 50

}

enemy_dict = {
    'name': enemy,
    'health': 100,
    'damage': yr

}

result=attack(player,enemy)

print("У атакуемого осталось: ")
print(str(result))