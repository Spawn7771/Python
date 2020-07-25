#Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
#С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.

import json, pickle

my_favourite_group = {
'name': 'Rammstein',
'tracks': ['Mutter', 'Radio','Mein Herz brennt', 'Du hast', 'Sonne', 'Frühling in Paris'],
'Albums': [{'name': 'Rosenrot','year': 2005},{'name': 'Sehnsucht','year': 1997},{'name': 'Liebe Ist Für Alle Da', 'year': 2009}]
}

print(type(my_favourite_group))

#сериализация в байты
my_fg=pickle.dumps(my_favourite_group)
print(my_fg) #вывод в терминал

#открываем файл
with open('group.pickle', 'wb') as f:
    # пишем объект в файл group.pickle в байт формате
    pickle.dump(my_favourite_group, f)


#открываем файл
with open('group.json', 'w', encoding='utf-8') as f:
    # пишем объект в файл group.pickle в формате json
    json.dump(my_favourite_group,f)

#сериализация в json
json_group = json.dumps(my_favourite_group)
print(json_group) #вывод в терминал