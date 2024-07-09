import random
import math
a = [[random.randint(1, 10) for j in range(4)] for i in range(5)]
b = [[math.factorial(a[i][j]) for j in range(4)] for i in range(5)]
for linha in a:
    print(a)
for linha in a:
    print(b)
#random é o módulo que contém a função randint
#math é o módulo que contém a função factorial
