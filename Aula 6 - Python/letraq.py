a = []
b = []
for i in range (15):
    a.append(float(input(f"Digite o {i+1}° numero: ")))
    if i % 2 == 0:
        b.append(a[i]/2)
    else:
        b.append(a[i]*1.5)
print(a)
print(b)