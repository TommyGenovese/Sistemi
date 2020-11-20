import math

number2char = {}
char2number = {}
for i in range (65,91):
    char2number[chr(i)] = i - 65
    number2char[i-65] = chr(i)

def is_prime(n):

    """
    n:          number to check
    
    returns:    -0: number not prime
                -1: number prime
    """

    #n is the prime number to find out
    bruteforce_numbers = []
    for i in range (2,int(math.sqrt(n) + 1)):
        bruteforce_numbers.append(i)
    
    for number in bruteforce_numbers:
        if n != number and n % number == 0:
            return 0

    return 1

def euclide(a,b):
    """
    a,b:        number to use
    
    returns:    MCD of a and b
    """

    if b > a:
        a,b = b,a

    while True:
        newa = a % b
        if newa == 0:
            return b
            break
        else:
            a = b
            b = newa

def generate_keys():

    #INSERTING PRIME NUMBERS
    while True:
        p,q = input("Insert (P,Q)>> ").split(",")
        p = int(p)
        q = int(q)

        if is_prime(p) and is_prime(q) and p > 1 and q > 1:
            print("numbers ok")
            break
    
    #CALCULATING n & m
    n = p*q
    print(f"n = {n}")
    
    m = int(((p-1)*(q-1))/euclide(p-1,q-1))
    print(f"m = ({(p-1)*(q-1)}) / {euclide(16,10)} = {m}")

    #CALCULATING c NUMBERS AND ASK USER TO CHOSE ONE
    c_list = []
    for i in range(2,m+1):
        if euclide(i,m) ==1:
            c_list.append(i)

    while True:
        c = int(input(f"Chose c {c_list}>>"))
        if c in c_list:
            break
    
    #CALCULATING d NUMBERS AND ASK USER TO CHOSE ONE
    d_list = []
    for i in range(1,81):
        if ((37*i) % 80) == 1:
            d_list.append(i)
    
    while True:
        d = int(input(f"Chose d {d_list}>> "))
        if d in d_list:
            break
    print(m)
    return n, c, p, q, m, d

def main():
    n, c, p, q, m, d = generate_keys()

    print(f"""
        PUBLIC KEYS
            -n:     {n}
            -c:     {c}
        PRIVATE KEYS
            -p:     {p}
            -q:     {q}
            -m:     {m}
            -d:     {d}
    """)
    
    msg = input("MSG>> ")
    msg = msg.upper()

    cifred_msg = []
    number_msg = []
    for a in msg:
        number_msg.append(char2number[a])
        print(char2number[a])
        cifred_msg.append(int((char2number[a]**c) % n))
    
    print(f"cifred msg = {cifred_msg}")
    print(f"number msg = {number_msg}")

    decifred_msg = ""
    for b in cifred_msg:
        decifred_msg = decifred_msg + str(number2char[int((b**d) % n)])
    print(decifred_msg)

if __name__ == "__main__":
    main()