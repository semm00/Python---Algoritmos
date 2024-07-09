a = []
b = []
cont = 0
while cont < 5:
    n=int(input(f"Digite o {cont+1}° numero: "))
    if n>0:
        a.append(n)
        b.append(a[cont]*-1)
        cont+=1
    else:
        print("Numero invalido, digite um numero positivo.")
print(a)
print(b)