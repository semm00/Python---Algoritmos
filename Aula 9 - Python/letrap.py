import random
a = [[random.randint(1, 10) for j in range(7)] for i in range(10)]
p = 0 
im = 0
for i in range(10):
    for j in range(7):
        if a[i][j] % 2 == 0:
            p += 1
        else:
            im += 1
            
print("O total de números pares na matriz é:", p)
print("O total de números ímpares na matriz é:", im)
print("O percentual de números pares na matriz é:", p*100/70, "%")
print("O percentual de números ímpares na matriz é:", im*100/70, "%")
