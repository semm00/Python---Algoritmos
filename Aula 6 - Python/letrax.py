a = []
b = []
for i in range (4):
    a.append(float(input(f"Digite o {i+1}° numero: ")))
for c in range (4):
    if c % 2 != 0 and i % 2 == 0:
        b.append(a[i])
    if c % 2 == 0 and i % 2 != 0:
        b.append(a[i])
print(a)
print(b)