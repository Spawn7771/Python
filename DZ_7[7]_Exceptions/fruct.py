#Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

fruct1=['яблоко','груша','киви','слива','ананас']
fruct2=['яблоко','мондарин','слива','груша']

fruct3=fruct1+fruct2

result= [fruct for fruct in fruct3 if fruct3.count(fruct)>1]

print(list(set(result)))