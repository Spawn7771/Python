#Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.


#Для проверки используйте вызовы функций (можно непосредственно проверить работу в модуле main.py)
#create_folders()
#remove_folders()

import os

def create_folders():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_path)



def remove_folders():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(new_path)

#create_folders()
#remove_folders()

