c = 1
while c <= 10:
    if c%2 !=0:
        f = 1
        for i in range(1, c+1):
                f *= i
        print("O fatorial de {} é {}".format(c, f))
    c+=1