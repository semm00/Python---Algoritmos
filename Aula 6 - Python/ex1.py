a = []
b = []
for i in range(1,6):
    a.append(int(input(f"Digite o {i}° numero: ")))
    if a[i-1]%2==0:
        b.append(a[i-1]+5) 
    else:
        b.append(a[i-1]*5)
print(a)
print(b)