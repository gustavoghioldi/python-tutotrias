name = "gustavo ghioldi"

print(name[0])
print(len(name))
print(name[1:5])
print(name[:5])
print(name[2:])
print(name[-1])
print(name*3)
print(name.startswith("F"))
print(name.startswith("g"))
print(name.capitalize())
print(name.upper())

name2= "       dkjksdjkjds      "
print(name2.strip())

print(name.split())
print(name.split("a"))
print(name.replace("gustavo", "gus"))

for i in name:
    print(i)
w = "mundo"
print("hola {}".format(w))
print(f"hola {w}") # esta es la que hay qu usar
print("hola", w)
print("hola "+w+"!")



