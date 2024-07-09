import random
import math

a = [[random.randint(1, 5) for j in range(7)] for i in range(7)]
b = []
for i in range(7):
    b.append([])
    for j in range(7):
        f=0
        if i==j and i%2==0:
            b[i].append(math.factorial(a[i][j]))
        else:
            for k in range(0,a[i][j]+1):
                f+=k
            b[i].append(f)
for linha in a:
    print(linha)

for linha in b:
    print(linha)