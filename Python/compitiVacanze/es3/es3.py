
#run line:  python es3.py es3_sample.txt
from sys import argv

script, filename = argv     #this line take parameters at the begin
# of the exercise (1° is the name of ex and 2°is the name of the file to open)

#open the file (filename)
txt = open(filename)

#print the content of the filename (every line)
print(f"\nHere's your file {filename}:\n")
print(txt.read())

#ask again which file u want to open
print("\nType the filename again:")
file_again = input("> ")

#same of the one above (line 6)
txt_again = open(file_again)

print(txt_again.read())

