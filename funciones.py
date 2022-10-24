from math import sqrt as cuadrado 
from datetime import datetime

print("HOLA")
print(cuadrado(9))
print(datetime.now())
print(type(datetime.now()))

# funciones definidas por nosotros
def saludo(name=None, lang="ES"):
    if not name:
        name = "Anonimo"
    return f"Hello {name}" if lang != "ES" else f"Hola {name}"

print(saludo("Gustavo", "EN"))
print(saludo("Gustavo", "ES"))   
print(saludo("Gustavo"))
print(saludo())
print(saludo(lang='EN', name="Juan"))

def test (name, *args,  lang="ES",**kwargs):
    print(name)
    print(lang)
    print(args)
    print(kwargs)

test("gus", 1, 2, 3, "assasa" , hola=12, chau = 16)    

