#Listas
lista = [1, 2, 3, "aasdasd", [1, 2, 3], True, None, 1, 2, 3, 1]
print(lista[2]) # me trae la posicion 3
print(len(lista))
lista[3] = "lo cambie"
lista.append(999.99) # agrega un elemento al final de la lista
del lista[10] #borra la posicion 11
print(lista)
lista.insert(2, "HOLA")

for i in lista:
    print(i)

print(1 in lista)
print("chau" in lista)
print("-- fin listas --")
