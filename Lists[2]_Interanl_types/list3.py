my_list_1 = [2,2,5,12,8,2,12]
r = my_list_1.sort()
r = [my_list_1[0]]
i=1
z=0

while i < len(my_list_1):
    if r[z] != my_list_1[i]:
        r.append(my_list_1[i])
        z += 1
    i += 1

print (r)

