def adj2dict(matrice):
    dictionary = {}
    for n in range(len(matrice)):
        dictionary[n]=matrice[n]
    return dictionary

def dict2adj(diz):
    matrix= []
    for _, i in diz.items():
        matrix.append(i)
    return matrix

def user2dictPes():
    nodi = int(input("Inserire numero di nodi: "))
    matrix = []
    for i in range(0,nodi):
        neighbor = [int(n) for n in input(f"Inserisci i pesi dei collegamneti fra i nodi in ordine {i+1}: ").split(",")]
        colonne = [0 for n in range(0,nodi)]
        for n in neighbor:
            if(n != -1):
                colonne[n] = 1
        matrix.append(colonne)
    return matrix


#main
mat= [[2],[1,3]]
diz=adj2dict(mat)
print(f"\nfStampa del dizionario ottenuto da adj2dict:\n{diz}\n")
mat = dict2adj(diz)
print(f"ora stampiamo la matrice ottenuta da dict2adj: \n{mat}\n")

print(user2dictPes())
