import random
a = [[random.randint(-10,40) for j in range(5)] for i in range(4)]
b = []
for i in range(4):
    b.append([])
    for j in range(5):
        b[i].append((9*a[i][j]+160)/5)
print(a)
print(b)