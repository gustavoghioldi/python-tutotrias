class Person:
    def __init__(self, uid, first_name, last_name):# metodo constructor
        print("me crearon")
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.entradas = 0
    
    def add_entradas(self)->None:
        self.entradas += 1

p1 = Person(25724484, "Gustavo", "Ghioldi")
p2 = Person(25724484, "Gustavo", "Ghioldi")

print(type(p1))
print(id(p1))
print(id(p2))
print(f"id: {p1.uid}, name: {p1.first_name} {p1.last_name}")
p2.uid = 33333 # de esta manera cambio el valor de los atributos
print(f"id: {p2.uid}, name: {p2.first_name} {p2.last_name}")
print(p1.entradas)
p1.add_entradas()
p1.add_entradas()
p1.add_entradas()
p1.add_entradas()
print(p1.entradas)