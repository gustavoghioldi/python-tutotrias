#dict  // es un JSON(pero distinto)

dic = {
    "nombre": "Gustavo",
    "id" : {
        "nro": 25724484,
        "type": "DNI"
    },
    "edad": 45,
    "saldo": 100.99,
    "active_user": True
}

print(dic["nombre"])

for i in dic:
    print(dic[i])

dic["lenguaje"] = "Python"
print(dic)

del dic["nombre"]

print(len(dic))