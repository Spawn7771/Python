#Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:

#    Наносит урон. Это улучшенная версия функции из задачи 3.

#   Вычисляет урон по отношению к броне.

#   Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

def attack(player, enemy):
    zdorovie = player_dict['health']
    yron = enemy_dict['damage']
    def zachita(damage=40, armor=1.2):
        armor2 = player_dict['armor']
        yron4 = yron / armor2
        res = zdorovie - yron4
        return res
    return zachita

player= input("Введите имя атакуемого: ")
enemy =  input("Введите имя атакуещего: ")
zdor =  int(input("Введите кол-во здоровья атакуемого: "))
yr =  int(input("Введите урон атакуещего: "))


player_dict = {
    'name' : player,
    'health': zdor,
    'damage': 50,
    'armor': 1.2

}


enemy_dict = {
    'name': enemy,
    'health': 100,
    'damage': yr,
    'armor': 1.2

}

result=attack(player,enemy)
print("У атакуемого осталось: ")
print(result())