#esercizio con pile e parentesi su python

def push(stack, element):
    stack.append(element)
    return stack            

def pop(stack):
    element = stack.pop()
    return stack, element   #returna due oggetti

pila = [2, 3, 6, "ciao"]
pila = push(pila, 5)
print(pila)
pila,_ = pop(pila)
print(pila)