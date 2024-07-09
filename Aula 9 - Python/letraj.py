import random
a = [[random.randint(1, 10) for j in range(5)] for i in range(6)]
b = []
for i in range (6):
    b.append([])
    for j in range(5):
        if a[i][j] % 2 == 0:
            b[i].append(a[i][j]+5)
        else:
            b[i].append(a[i][j]-4)
            
for linha in a:
    print(linha)

for linha in b:
    print(linha)