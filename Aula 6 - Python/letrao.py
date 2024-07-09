a = []
b = []
for i in range(25):
    a.append(float(input(f"Digite o {i+1}° numero: ")))
    b.append((9*a[i]+160)/5)
print(a)
print(b)

