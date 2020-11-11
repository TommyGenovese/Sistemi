#scrivere un programma che riempie una lista arbitraria chiedendo
#i valori degli elemnti all'utente.

ancora = True
l1 =[]
if(input("vuoi un numero(S per il si)")== 'S'):
    ancora=True

while(ancora == True):
    l1.append(input("inserisci un numero nella lista"))
    if(input("vuoi un numero (S per il si)")== 'S'):
        pass
    else:
        ancora=False
    
print(l1)

