import random
import math
a=[random.randint(1,10) for i in range(4)]
b=[random.randint(1,10) for i in range(4)]
c=[random.randint(1,10) for i in range(4)]
d=[random.randint(1,10) for i in range(4)]
e=[[0 for j in range(4)] for i in range(4)]

for i in range(4):
    e[0][i] = 2 * a[i]
    e[1][i] = 3 * b[i]
    e[2][i] = 4 * c[i]
    e[3][i] = math.factorial(d[i])

print(a)
print(b)
print(c)
print(d)

for linha in e:
    print(linha)
    
