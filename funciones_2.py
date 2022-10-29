def suma(a , b):
    return a + b

def resta(a, b):
    return a - b

division = lambda a, b: a / b
mult = lambda a, b: a * b

def operation(a  , b, op):
    return op(a, b)

# podemos pasar una funcion como parametro
result = operation(1, 3, suma)
print(result)
print(operation(1, 3, resta))
print(operation(2, 3, division))

name = lambda x : x+100
print(name(1))
