a=[]
b=[]
c=[]
for i in range (0,20):
    a.append(int(input(f"Digite o {i+1}° numero de a: ")))
for j in range (0,30):
    b.append(int(input(f"Digite o {j+1}° numero de b: ")))
c = a + b
print(a)
print(b)
print(c)