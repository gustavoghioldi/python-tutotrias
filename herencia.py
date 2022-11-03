class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def run(self):
        print("i can run")

    def can_ride(self):
        return False
    def can_fly(self):
        return False
    def can_swim(self):
        return False

class Car(Vehicle):
    def run(self):
        print("i can ride")
    def can_ride(self):
        return True
    
class Plane(Vehicle):
    def can_fly(self):
        return True
    def run(self):
        print("i can fly")

class Boat(Vehicle):
    def can_swim(self):
        return True
    def run(self):
        print("i can swim")

car = Car("red")
print(car.get_color())
car.run()
print(car.can_fly())
print(car.can_ride())
print(car.can_swim())

plane = Plane('blue')
print(plane.get_color())
plane.run()
print(plane.can_fly())
print(plane.can_ride())
print(plane.can_swim())

bote = Boat('yellow')
bote.run()
print(bote.can_fly())
print(bote.can_ride())
print(bote.can_swim())

class Anfibio(Car, Boat):
    def __init__(self, kg):
        self.__kg = kg
        super().__init__("black") # sobre escribe el constructor

    def get_kg(self):
        return self.__kg

print("------------")
anfi = Anfibio(2500)
print(anfi.can_fly())
print(anfi.can_ride())
print(anfi.can_swim())
print(anfi.get_color())
print(anfi.get_kg())


## emular sobrecarga de metodos.
class Persona:
    def caminar (self, edad, peso=None):
        if peso == None:
            print("camina de una manera")
        else:
            print("camina")