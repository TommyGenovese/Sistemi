#creare un programma per i nodi


nodi= input("inserisci il numero di nodi: ")
for i in nodi:
    viciniTot = input(f"inserisci i vicini del nodo {i+1} (separati con una vircola)")
    viciniTot = viciniTot.split(",")
    


for i in nodi:
    print(f"il nodo {i+1} ha {len(viciniTot)} nodi")
    



    




#mat = [[0,1,1], [1,0,0], [0,1,0]]
#for k in 0:3:
#    print(f"il nodo numero{k+1} è in collegamento con i nodi numero:")
#    for i in :
#        if(mat[1][i]==1):
#            print(i)

