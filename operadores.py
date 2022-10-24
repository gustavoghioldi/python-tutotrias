a = 3
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) # "a" elevado a la "b"
print(a%b) # modulo o resto
print(a//b) # division de enteros

a += b # a = a + b
print(a)

print(a > b)
print(a < b)
print(a == b)
print(a != b) #distinto
print(a >= b)
print(a <= b)

a = {"1":"10!"}
b = {"1":"10!"}
print(id(a))
print(id(b))
print(a == b)
print (a is b)

print(saludo:="Hola") # no lo usen
print(saludo) # no lo usen

print(True and False) # lo 2 o mas deben ser True 
print(True or False) # con solo un valor True es True
print(not True)

# los positivos son verdaderos y 0 <= Falsos 
c = [1, 2, 3]
if len(c):
    print("hola")