import sys

print(sys.argv)
try:
    print (sys.argv[13])
except IndexError:
    print("no existe la posicion 13")
for i in sys.argv:
    print(i)