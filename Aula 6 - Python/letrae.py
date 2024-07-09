a = []
b = []
for i in range (0,5):
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    f=1
    for c in range (1, a[i]+1):
        f*=c
    b.append(f)
print(a)
print(b)