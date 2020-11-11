#date due liste scelte dall'utente trovare gli elemnti comuni e inserirli in una terza lista

l1=["hola", "12", "rosa", "gg"]
l2=["ciao", "12", "fiore", "wp"]
l3 = []

#algoritmo
for i1 in l1:
    if i1 in l2:
        l3.append(i1)
print(l3)
        
