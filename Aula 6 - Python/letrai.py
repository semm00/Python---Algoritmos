a=[]
b=[]
c=[]
d=[]
for i in range (0,5):
    a.append(int(input(f"Digite o {i+1}° numero de a: ")))
for j in range (0,5):
    b.append(int(input(f"Digite o {j+1}° numero de b: ")))
for y in range (0,5):
    c.append(int(input(f"Digite o {y+1}° numero de c: ")))
d = a + b + c
print(a)
print(b)
print(c)
print(d)