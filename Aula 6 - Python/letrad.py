a = []
b = []
for i in range (0,15):
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    b.append(a[i]**2)
print(a)
print(b)