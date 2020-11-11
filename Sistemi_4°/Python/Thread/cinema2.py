

import threading as thr
import time 
import random
import logging

MAXP = 3
pin = 0

s  = thr.Lock()

def cassa(numero):

    s.acquire()

    rdm = random.randint(1,1000)
    time.sleep(random.randint(1,3))

    return rdm

def negozio(numero):

    global pin

    rdm = cassa(numero)
    s.release()

    print(f"\bSono il cliente {numero} e ho speso {rdm}, ora me ne vado soddisfatto")

    pin -= 1

def cliente(i):

    global pin
    global MAXP

    if(pin == MAXP):
        print(f"\b Cliente {i} cacciato dal supermercato")
    else:
        pin += 1
        negozio(i)




rdm = random.randint(4,24)

t = [rdm]

t = [thr.Thread(target=cliente, args=(i+1,)) for i in range(0,rdm)]

for i in t:
    i.start()
    time.sleep(1)

for i in t:
    i.join()

