import os, shutil, datetime

# Функция создания файла

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Функция создания папки

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')

# Функция просмотра директории с возможностью просмотра только папок

def get_list(folders_only=False):
        result = os.listdir()
        if folders_only:
            result = [f for f in result if os.path.isdir(f)]
        print(result)

# Функция удаления папок и файлов

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

# Функция копирования

def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)

#Функция записи текущего времени обращения

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

#Функция смены текущей директории

#def change_dir():
#    cwd = os.getcwd()
#    print (f'Ваша текущая рабочая директория {cwd}')
#    print('Введите новую рабочую директорию для смены, по форме текущей')
#    os.chdir(input())
#    print("Теперь текущая директория изменена на ", os.getcwd())

def change_dir(path):
    if os.path.exists(path):
        os.chdir(path)
        print("Теперь текущая директория изменена на ", os.getcwd())
    else:
        print("Невозможно изменить текущую директорию, т.к. такой директории нет")


def ygad_chislo():
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

if __name__=='__main__':
    #create_file('text.dat')
    #create_file('text1.dat', 'some text')
    #create_folder('new_folder')
    #get_list(True)
    #delete_file('text.dat')
    #copy_file('text.dat','text2.dat')
    #save_info('test')
    #ygad_chislo()
    change_dir("/home/spawn")