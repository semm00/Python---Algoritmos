import random
a = [[random.randint(1, 10) for j in range(6)] for i in range(8)]
b = []
sl=0
sm=0
for i in range(8):
    sl=0
    for j in range(6):
        sl+=a[i][j]
    b.append(sl)
    sm+=sl
    

for linha in a:
    print(linha)

print("essa é a matriz b:", b)
print("esse é o somatório dos elementos da matriz b:", sm)