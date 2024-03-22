resp="sim"
while resp=='sim':
    num=int(input("Digite um valor:"))
    r=num*3
    print(r)
    resp=input("Deseja continuar? ")
    if resp!="sim": #exclamação = a diferente
        break
print("Fim do programa")