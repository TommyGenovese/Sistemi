import threading as thread
import logging
import time 
import random

MAX_PERS = 5

#persone nel market
PerInMarket=0

m = thread.Lock()


def client(c):
    global MAX_PERS
    global PerInMarket

    #controllo se è stato raggiunto il numero amssimo di persone nel negozio
    if (PerInMarket==MAX_PERS):
        print(f"Mi spiace cliente {c}, il negozio ha raggiunto il numero massimo")
    else:
        PerInMarket = PerInMarket + 1
        #2 secondi nel negozio circa
        spesa = cassa(c)

        #esce dal negozio
        PerInMarket= PerInMarket-1

        print(f"Il cliente {c} ha speso {spesa} ed esce dal negozio")
        #esce dal negozio
        PerInMarket= PerInMarket-1

        m.release()
        print(f"Possono accedere solo più {MAX_PERS-PerInMarket} persone ")


def cassa(numb):
    #chiudo la cassa appena arriva il cliente
    m.acquire()

    #prezzo spesa effettuato
    ran = random.randint(1, 300)
    time.sleep(random.randint(1,3))
    
    return ran


#Main
ran = random.randint(4, 24)
#inizializzo i clienti
th = [ran]

th = [thread.Thread(target=client, args=(i+1,)) for i in range(0,ran)]

for i in th:
    i.start()
    time.sleep(1)

for i in th:
    i.join()
