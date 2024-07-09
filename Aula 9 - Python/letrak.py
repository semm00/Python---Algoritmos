import random
a = [[random.randint(1,10)for j in range(4)]for i in range(4)]
s=0
for i in range(4):
    for j in range(4):
        if i==j:
           s+=a[i][j]
print(s)
            
for linha in a: 
    print(linha)