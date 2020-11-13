#Author: Genovese Tommaso
#Date:11/11/2020
#es:Implementare l'algoritmo Euclide (cazz'è?): In ogni triangolo rettangolo il 
#   quadrato costruito su un cateto è equivalente al rettangolo che ha per
#   dimensioni l'ipotenusa e la proiezione di quel cateto sull'ipotenusa.
import time
a = int(input("Insert A value (bigger than the next ): "))
b = int(input("Insert B value (smaller than the previous one): "))
while(1):
    up_a = a % b   

    if up_a == 0:   
        print(f"The greatest common divisor is: {b}")
        break
    else:
        b=up_a
        a=b
        
time.sleep(3)