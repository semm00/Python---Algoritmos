import random
a = [[random.randint(1, 10) for j in range(7)] for i in range(7)]
t = 0 
for i in range(7):
    for j in range(7):
        if a[i][j] % 2 == 0:
            t += 1
print("O total de números pares na matriz é:", t)

for linha in a:
    print(linha)