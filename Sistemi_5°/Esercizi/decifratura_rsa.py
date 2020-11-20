lista = [459541, 134033, 243696, 243696, 497836, 121848, 497836, 252297, 243696, 357421]
n= 536131
c= 5939
mex= []

char2number={}
number2char={}


for i in range (65,91):
    char2number[chr(i)] = i - 65
    number2char[i-65] = chr(i)

for i in lista:
    msg = number2char((lista[i]**n)%c)
    mex.append(msg)

