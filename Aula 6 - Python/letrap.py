a = []
b = []
for i in range (0, 12):
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    if a[i] % 2 != 0:
        b.append(a[i]*2)
    else:
        b.append(a[i])
print(a)
print(b)