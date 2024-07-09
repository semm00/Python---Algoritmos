import random
a = [[random.randint(1,10)for j in range(5)]for i in range(5)]
b=[]
for i in range(5):
    b.append([])
    for j in range(5):
        if i==j:
            b[i].append(3*a[i][j])
        else: 
            b[i].append(2*a[i][j])

for linha in a:
    print(linha)

for linha in b:
    print(linha)