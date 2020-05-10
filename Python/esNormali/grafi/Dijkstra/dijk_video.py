mat= [[0,1,2,0],[1,0,3,1],[2,3,0,2],[0,1,2,0]]
INFI = 100000
def Dijkstra(matr, source):
    Q = []
    dist = []
    pred = []
    c=0

    dist=[INFI for _ in range(0,len(matr))]
    pred= ["non c'è" for i in range(0,len(matr))]      #non esistono
    Q= [i for i in range(0,len(matr))]

    dist[source] = 0
    scelto= source

    while len(Q)>0:
        print(f"\nPasso: {c}")
        print(f"Successori: {Q}")
        print(f"Distanze: {dist}")
        minn = INFI
        for i in Q:
            if(dist[i]<minn):
                minn = dist[i]
                scelto=i
        
        Q.remove(scelto)

        for v,w in enumerate(matr[Q]):
            if (dist[scelto]+w<dist[v]) and (w>0):
                dist[v] = dist[scelto] + w
                pred[i]=Q[i]
        c=c+1
    return dist, pred

def neighbor(mat, indice):
    matNeigh = []
    for i,c in mat:
        if (mat[i][c] == indice):
            matNeigh.append(mat[i][c])
    return matNeigh
def main():
    Dijkstra(mat, 0)

if __name__ =="__main__":
    main()