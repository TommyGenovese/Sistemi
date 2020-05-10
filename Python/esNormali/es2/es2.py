ancora = True
l1 =[]
if(input("vuoi una parola?(S per il si) ")== 'S'):
    ancora=True
k=0
LUNG = 5
while(ancora == True):
    k= k+1
    l1.append(input("inserisci una parola nella lista: "))
    if(input("vuoi una parola (S per il si) ")!= 'S'):
        ancora=False
l1.sort()
for i in l1:
    if len(i)>=LUNG:
        print(f"la parola {i} è più lunga di {LUNG}")


