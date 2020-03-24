diz={0:[0,0], 
    1: [4,0],
    2: [1,0],
    3: [5,1],
    4: [8,3],
    5: [9,4],
    6: [9,4],
    7: [11,6],
    8: [11,5],
    9: [12,8]
}
INFI = 100000

def Dijkstra(Graph, source):
    Q = []
    dist = []
    prev = []
    for v in enumerate(Graph):
        dist[v]=INFI
        prev[v]= None
        Q.append(v)

    dist[source] = 0

    while Q != None:
        minn = INFI
        for i in len(dist):
            if(dist[i]<u):
                minn = i
        u = [dist[minn], prev[minn]]
        Q.remove(minn)

        for v in vicini(minn):


def vicini(diz, indice):
    #for c in i:
    #    if (mat[i][c] > 0):
    #        if (mat[i][c+1] > 0):
    #            matNeigh.append(mat[i][c+1])
    #        if (mat[i-1][c] > 0):
    #            matNeigh.append(mat[i-1][c])
    #        if (mat[i][c-1] > 0):
    #            matNeigh.append(mat[i][c-1])
    #        if (mat[i+1][c] > 0):
    #            matNeigh.append(mat[i+1][c])
    #dictionary[i] = matNeigh







 

 













def adj2dict(matrice):
    dictionary = {}
    for n in range(len(matrice)):
        dictionary[n]=matrice[n]
    return dictionary

#def dict2adj(diz):
#    matrix= []
#    for _, i in diz.items():
#        matrix.append(i)
#    return matrix

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
print(user2dictPes())
