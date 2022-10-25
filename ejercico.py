def promedio (*args):
    l = len(args)
    total = 0 
    for num in args:
        total += num
    return total/l

print(promedio(2, 3, 4, 10, 20, 100, 1, 1, 1))
