a, b, c = [], [], []
cont = 0
print("Inserido elementos na lista a")
while cont<6:
    n = (int(input("Digite um numero par: ")))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("Esse numero é impar!")
print("Inserido elementos na lista b")
cont = 0
while cont<6:
    n = (int(input("Digite um numero impar: ")))
    if n%2!=0:
        b.append(n)
        cont+=1
    else:
        print("Esse numero é par!")
c=a+b
print(c)
        