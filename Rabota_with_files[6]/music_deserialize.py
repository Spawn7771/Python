import json, pickle

# открываем файл
with open('group.pickle', 'rb') as f:
    # читаем объект из файла с помощью pickle
    my_fg = pickle.load(f)

print(my_fg)

with open('group.json', 'r') as f:
    my_fg2 = json.load(f)

print(my_fg2)
