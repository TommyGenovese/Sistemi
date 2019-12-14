"""
documento il programma
bla bla bla
"""

def somma(a,b):     #def: definisce la funzione somma
    return a+b

lista = [1,"ciao",3, somma(3,4), somma]
x = somma(10, 8)

posizione = 1
print(lista[0:3])

j = len(lista)
print(j)


#for i in lista:
#    print(i+1)


lista= [10,3, -4, 6]
lista[2:4]                       #slicing di liste

lista2 = lista[1:4:2]            #il terzo numero indica che ne prende 1 ogni 2 numeri


l = [1,2,3]
l.append(4)     #aggiunge il numero 4 in fondo alla lista
print(l)        #stampa: 1 2 3 4

l.count(2)      #dato un elemento ti dice quante volte compare nella lista

l.sort()        #riordina la lista, non returna niente

l.reverse()     #inverte tutti gli elementi della lista

l.copy()





