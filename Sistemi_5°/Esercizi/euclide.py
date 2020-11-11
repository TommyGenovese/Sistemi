#Author: Genovese Tommaso
#Date:11/11/2020
#es:Implementare Euclide (cazz'è?): In ogni triangolo rettangolo il 
#   quadrato costruito su un cateto è equivalente al rettangolo che ha per
#   dimensioni l'ipotenusa e la proiezione di quel cateto sull'ipotenusa.

a = int(input("Inserisci il valore di A(più grande del successivo): "))
b = int(input("Inserisci il valore di B(più piccolo del precedente): "))
while(1):
    up_a = a % b    
    if up_a == 0:   
        print(f"il valore di b è: {b}")
        break
    else:
        a=b
        b=up_a
