import random
a = [[random.randint(1,20) for j in range(15)] for i in range(15)]
s=0
for i in range(15):
    for j in range(15):
        if i==j:
            s+=a[i][j]
print(s)
            