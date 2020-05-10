#creare un programma per i nodi

def GraphOriented():
    nodi = int(input("Inserire numero di nodi: "))

    matrix = []

    for i in range(0,nodi):
        neighbor = [int(n) for n in input(f"Inserisci i nodi adiacenti a {i}: ").split(",")]
        colonne = [0 for n in range(0,nodi)]
        for n in neighbor:
            if(n != -1):
                colonne[n] = 1
        matrix.append(colonne)

    print(matrix)