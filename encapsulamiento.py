class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

v = Vehicle('red')
print(v.get_color())

class Account:
    def __init__(self, dni):
        self.__dni = dni #attributo privado uso __
        self.__total = 0 

    def get_dni(self):
        return self.__dni

    def get_total(self):
        return self.__total

    def set_total(self, amount, password):
        if password != '123':
            raise Exception("no tienes credenciales validas")
        self.__total = amount

    def add_account(self, amount):
        self.__total += amount

    def extract_account(self, amount):
        if self.__total - amount < 0:
            raise Exception("el monto queda debajo de cero")
        self.__total -= amount

    def __calcular(self):
        pass    

account = Account(24343434)
account.__calcular()
account.add_account(100)
account.extract_account(12)                           
print(account.get_total())
account.set_total(10000, '123')
print(account.get_total())
