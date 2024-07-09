a = []
b = []
for i in range (0,5):
    a.append(int(input(f"Digite o {i+1}° numero de a: ")))
b = a[:]
b.reverse()
print(a)
print(b)