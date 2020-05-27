import threading as thr
import time 
import random
import logging

filaA = 10
filaB = 6

biglietti = 100

def unlockA():

    if(filaA > 0):
        s.release()
    else:
        s1.release()

def unlockB():

    if(filaB > 0):
        s1.release()
    else:
        s.release()

unlock = {
    0 : unlockA,
    1 : unlockB 
}

def cassa1(i):

    s.acquire()
    global filaA
    global biglietti
    filaA = filaA-1

    nBigliet = random.randint(0,10)

    print(f"Sono il cliente {i} alla cassa 1 e voglio acquistare {nBigliet} biglietti")


    if(biglietti == 0):
        print("Biglietti acquistati 0\n")
    elif (biglietti>0 and nBigliet<=biglietti):
        print(f"Biglietti acquistati {nBigliet}\n")
        biglietti = biglietti - nBigliet
    elif (biglietti>0 and nBigliet>=biglietti):
        print(f"Biglietti acquistati {biglietti}\n")
        biglietti = 0


    print(f"Biglietti disponibili {biglietti} \n")

    nBigliet2 = random.randint(0,1)
    unlock[nBigliet2]()

def cassa2(i):

    s1.acquire()
    global filaB
    global biglietti
    filaB = filaB-1

    nBigliet = random.randint(0,10)

    print(f"Sono il cliente {i} alla cassa 2 e voglio acquistare {nBigliet} biglietti")


    if(biglietti == 0):
        print("Biglietti acquistati 0\n")
    elif (biglietti>0 and nBigliet<=biglietti):
        print(f"Biglietti acquistati {nBigliet}\n")
        biglietti = biglietti - nBigliet
    elif (biglietti>0 and nBigliet>=biglietti):
        print(f"Biglietti acquistati {biglietti}\n")
        biglietti = 0


    print(f"Biglietti disponibili {biglietti} \n")

    nBigliet2 = random.randint(0,1)
    unlock[nBigliet2]()

def Main():

    t1  = [10]
    t2 = [6]

    #conto alla rovescia 3-->1
    for i in range(0,3):
        logging.info("Apertura casse in %d \n",3-i)
        time.sleep(1)


    # t1-->cassa 1
    # t2-->cassa 2

    #for i in range(0,10):
        #t1 = thr.Thread(target=cassa1, args=())
    t1  = [thr.Thread(target=cassa1, args=(i+1,)) for i in range(0,10)]
    t2 = [thr.Thread(target=cassa2, args=(i+1,)) for i in range(0,6)]

    for i in t1:
        i.start()

    for i in t2:
        i.start()

    for i in t1:
        i.join()
    
    for i in t2:
        i.join()
    
    print("Acquisto terminato")

if __name__ == '__main__': 

    format= " %(asctime)s : %(message)s "
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    s = thr.Lock()
    s1 = thr.Lock()

    s1.acquire()

    Main()
     