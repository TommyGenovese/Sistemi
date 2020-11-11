#.format sulle stringhe, 5 punti in cui una stringa è messa dentro un'altra
types_of_people = 10
#assegno ad x la stringa con all'interno la variabile types_of_peole
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)