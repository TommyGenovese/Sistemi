from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#wait the input(Return)
input("?")

#open the file in write mode(w)
print("Opening the file...")
target = open(filename, 'w')

#delate all the content of the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#create 3 variables and give a line (input) to each one
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#scrive riga per riga ciò che ho dato in input("line 1/2/3:"  escluso)
target.write(line1)
#per dividere le riga usa un semplice \n
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#chiude normalmente il file
print("And finally, we close it.")
target.close()