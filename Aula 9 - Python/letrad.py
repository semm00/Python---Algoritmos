a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(10):
    f=1
    b.append([a[i]+5])
    for j in range(a[i]):
        f*=j+1
    b[i].append(f)
    b[i].append(a[i]**2)          
print(a)
print(b)