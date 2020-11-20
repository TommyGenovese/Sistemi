#Author: Genovese Tommaso-
#Date: 11/11/2020
#es: Dato un numero, scomporlo in fattori primi.
import math, time
def num_primo(n):
    lista_num = []
    for k in range (2,int(math.sqrt(n) + 1)): #
        lista_num.append(k)
    for numb in lista_num:
        if (n != numb) and (n % numb == 0):
            return 0
    return 1


#main

n = int(input("insert the number: "))
if num_primo(n):
    print("Your number is already a prime number")
    print(n)
else:
    ListFact = []
    current = n
    for i in range(2,int(n/2)+1):
        #j = 1
        j=1
        while j==1:
            if (current % i) == 0:
                ListFact.append(i)
                current = current / i
            else:
                j = 0
    print(f"The number has been broken down: {ListaFatt}")

time.sleep(500)



