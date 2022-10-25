#Tuplas : son colo las listas pero inmutables
tupla = ("hola", "chau", 1, 2, True, None)
print(len(tupla))
print(type(tupla))
for i in tupla:
    print(i)

print(tupla[0])    
a, b, c, d, e, f = tupla # pasa los valores de la tupla a variables individuales
print(c)

print(tupla[-2]) # me trae el pen ultimo

print(tupla[1:4])
print(tupla[1:])
print(tupla[:4])