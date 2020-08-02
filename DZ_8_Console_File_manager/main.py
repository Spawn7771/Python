import sys, os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, ygad_chislo, change_dir
save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла/папки')
    except FileNotFoundError:
        print('Отсутствует файла/папка которую вы хотите удалить')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
            print('Отсутствует название папки, проверьте что вы написали папку для копирования и новую папку куда скопировать')
    else:
        copy_file(name,new_name)
elif command == 'chislo':
    ygad_chislo()
elif command == 'newdir':
    try:
        path=sys.argv[2]
        change_dir(path)
    except OSError:
        print("Невозможно изменить директорию")
    except IndexError:
        print("Вы не ввели директорию")
    except PermissionError:
        print("Не хватате прав доступа")

elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - ссоздание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('chislo - игра угадай число, вы загадываете число в уме а компьютер угадывает')
    print('newdir - изменить рабочую директорию')

save_info('Конец')