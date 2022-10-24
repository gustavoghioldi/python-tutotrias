# if 
a = 25

if a > 65:
    print("sos adulto mayor")
elif a >=18:
    print("sos mayor")
else:
    print("sos menor")

nom = "gus"
if not (nom == "no gus"):
    print("GUS")

lang = "ES"
saludo = "Hello" if lang != "ES" else "HOLA" 
print(saludo)

#while <- mientras
x = 0
while x < 10:
    print(x)
    x += 1