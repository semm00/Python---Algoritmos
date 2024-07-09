import random
a = [[random.randint(1, 10) for j in range(4)] for i in range(5)]
b = []
for i in range(5):
    b.append([])
    for j in range(4):
        f=1
        for k in range(1,a[i][j]+1):
            f*=k
        b[i].append(f)
print(a)
print(b)
