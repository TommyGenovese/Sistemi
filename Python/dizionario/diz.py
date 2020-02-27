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

#main
mat= [[2],[1,3]]
diz=adj2dict(mat)
print(f"\nStampa del dizionario ottenuto da adj2dict:\n{diz}\n")
mat = dict2adj(diz)
print(f"ora stampiamo la matrice ottenuta da dict2adj: \n{mat}\n")
