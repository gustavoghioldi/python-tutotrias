from funciones import saludo

with open("texto.txt", "w") as f: #puede ser w para escibir, r para leer , a para agregar
    f.write("HOLA COMO ESTAN??????\r")
    f.write("HOLA COMO ESTAN??????\r")
    f.write("HOLA COMO ESTAN??????\r")
    f.write("HOLA COMO ESTAN??????\r")
    f.write("HOLA COMO ESTAN??????\rcocoocococoococo\r")

# esta manera no se usa mas
f = open("texto2.txt", "w")
f.write("aca")
f.close()

with open("texto.txt", "a") as f: # attach
    f.write("HOLA!!!")

with open("texto.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())

print(saludo("GUstavo"))


