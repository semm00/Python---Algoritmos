import random
a = [[random.randint(1,10)for j in range(5)]for i in range(5)]
s=0
for i in range(5):
    for j in range(5):
        if i==j and i%2==0 and j%2==0:
           s+=a[i][j]
print(s)
            
for linha in a: 
    print(linha)