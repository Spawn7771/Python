#Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def opisanie(name,age,city):
    return  (name,age,city)


name=input("Введите имя: ")
age=input("Введите возраст: ")
city=input("Введите город проживания: ")

result=opisanie(name,age,city)

text = f'{name},{age}, проживает в городе {city}.'.format(result)

print(text)
