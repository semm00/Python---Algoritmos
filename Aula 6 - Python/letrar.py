a = []
b = []
c = []
d = []
for i in range (6):
    a.append(int(input(f"Digite o {i+1}° numero da lista a: ")))
    b.append(int(input(f"Digite o {i+1}° numero da lista b: ")))
    if i % 2 != 0:
        c.append(a[i])
        c.append(b[i])
    else:
        d.append(a[i])
        d.append(b[i])
print(a)
print(b)
print(c)
print(d)