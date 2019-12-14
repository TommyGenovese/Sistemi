
nameList=["Mario Rossi", "Luca Verdi", "Maria Vergine"]

for num, student in enumerate(nameList):
    print(f"{num} - {student}")

#scambio:
a =10
b = 5
print(f"a:{a}, b: {b}")
a, b = b, a
print(f"a:{a}, b: {b}")