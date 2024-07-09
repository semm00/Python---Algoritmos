a=[]
b=[]
c=[]
for i in range (0,10):
    a.append(int(input(f"Digite o {i+1}° numero de a: ")))
    b.append(int(input(f"Digite o {i+1}° numero de b: ")))
    c.append((a[i]+b[i])**2)
print(a) 
print(b)
print(c)