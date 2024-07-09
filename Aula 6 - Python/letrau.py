a, b, c = [], [], []
cont = 0
print("Inserido elementos na lista a")
while cont<3:
    n = (int(input("Digite um numero divisível por 2 ou 3: ")))
    if n%2 == 0 or n%3 == 0:
        a.append(n)
        cont+=1
    else:
        print("Esse numero é NÃO é divisível por 2 ou 3!")
print("Inserido elementos na lista b")
cont=0
while cont<3:
    n = (int(input("Digite um numero que NÃO mutiplo de 5: ")))
    if n%5 != 0:
        b.append(n)
        cont+=1
    else:
        print("Esse numero é multiplo de 5!")
c=a+b
print(c)