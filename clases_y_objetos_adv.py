class Stereo:
    def __init__(self, name:str)->None:
        self.name = name

class Paint:
    def __init__(self, color:str, opacity:int)->None:
        self.color = color
        self.opacity = opacity
    
    def get_description(self)->str:
        return f"{self.color} & {self.opacity}"   

class Car:
    def __init__(self, stereo: Stereo, paint: Paint)->None:
        self.stereo = stereo
        self.paint = paint

    def is_opacity(self)->bool:
        return True if self.paint.opacity > 50 else False

    def get_description(self, complete:bool=False)->str:
        if complete:
            return f"{self.stereo.name} & {self.paint.get_description()}"
        else:
            return f"{self.stereo.name} & {self.paint.color}"
    def get_stereo(self)-> Stereo:
        return self.stereo
        
s1 = Stereo("Phillips")
p1 = Paint("red", 33)
p2 = Paint("Blue", 55)

car1 = Car(s1, p1)

print(car1.paint.color)
print(car1.is_opacity())

car1.paint = p2
print(car1.is_opacity())
print(car1.paint.get_description())
print(car1.get_description())
print(car1.get_description(complete=True))