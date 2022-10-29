# captura
print("HOLA")
try:
    x = 10 / 0
    (1,3, 4, )[100]
    print(x)
except ZeroDivisionError:
    print("no se puedo devidir por cero")
except IndexError:
    print("error en el indice ")
except Exception:
    print("No se que paso")
print("chau")

#lanzar
class NoQuieroException(Exception):
    def __init__(self, message="oh h oho h"):            
        super().__init__(message)

def q_o_n(anyos):
    if anyos>50:
        raise NoQuieroException
    else:
        return "Si quiero"
try:
    print(q_o_n(50))
except NoQuieroException:
    print("Alguien no quiere")

q_o_n(99)    
raise(TypeError("Tipo equivocado"))