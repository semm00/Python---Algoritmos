a = []
b = []
for i in range (0,8):
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    b.append(a[i]*3)
print(a)
print(b)