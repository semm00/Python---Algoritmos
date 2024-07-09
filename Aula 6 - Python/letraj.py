a = []
b = []
for i in range (0,5):
    s=0
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    for j in range(a[i]+1):
        s+=j
    b.append(s)
print(a)
print(b)
    
