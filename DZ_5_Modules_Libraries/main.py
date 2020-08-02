#Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
#Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.


#----------------------------
import module1, module2

module1.create_folders() #Если запустить сразу create_folders() и
module1.remove_folders() #remove_folders() то вы ничего не увидете, т.к. папки будут созданы и тут же удалены

module2.rand_element(1,2,3,4,5)
#module2.rand_element()
#---------------------------------



#Вариант 2

#from module1 import *

#create_folders()
#remove_folders()


#Вариант 3

#from module2 import rand_element

#rand_element(1,2,3,4,5)
#rand_element()


