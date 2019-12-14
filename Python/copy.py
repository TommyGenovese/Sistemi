l1 =[1,2,3,4]
l2 = l1         #fa si che l2 PUNTI a l1
l1.append(9999)
print(l2)

l2 = l1[:]      #copia la lista l1 in l2, non la punta
