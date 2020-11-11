#esercizio della verifica fatta in C
import random
def push(stack, element):
    stack.append(element)
    return stack            

def pop(stack):
    element = stack.pop()
    return stack, element   #returna due oggetti

def mix(stack):
    for _ in range (0,10000):
        coppa = random.randint(5,45) #scelgo un punto per coppare
        mazzo1 = stack[0:coppa] + stack[coppa:]
    print("mazzo mescolato: ")
    return mazzo1

class carta(object):

    def __init__(self, seme, numero):
        self.seme = seme
        self.numero = numero
    def stampa(self):
        print(f"Carta ha come seme {self.seme}, numero {self.numero}")        

mazzo = []

Semi = ["C", "P", "D", "F"]

#creazione mazzo
for i in range(1, 14):
    for s in Semi:
        push(mazzo, carta (s, i))

for c in mazzo:
    c.stampa()

#coppare le carte
coppa = random.randint(1,52) #scelgo un punto per coppare
print(coppa)
mazzo1 = mazzo[0:coppa]
mazzo1 = mazzo[coppa:] + mazzo1[0:coppa]
print("mazzo randomizzato: ")
for c in mazzo1:
    c.stampa()


#mescolare il mazzo 
mazzo1 = mix(mazzo)

for c in mazzo1:
    c.stampa()
