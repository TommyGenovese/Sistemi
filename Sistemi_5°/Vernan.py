diz={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'L':9,'M':10,'N':11,'O':12,'P':13,'Q':14,'R':15,'S':16,'T':17,'U':18,'V':19,'Z':20}
Chiave= "T-O-M-M-A-S-O-G-E-N-O-V-E-S-E"
Messaggio="C-I-A-O-S-O-N-O-T-O-M-M-Y"
default='-'
ChiaveNum=''
Chiave= Chiave.split("-")
print(Chiave)

for i in range(0, 15):
    num=(diz.get(Chiave[i], default))
    ChiaveNum= Chiave + str(num)

print(ChiaveNum)