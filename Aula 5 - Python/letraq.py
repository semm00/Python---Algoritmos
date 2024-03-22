s=0
while True:
    co = str(input("Digite o nome do cômodo: "))
    l = int(input("Digite a largura do cômodo (SI): "))
    cp = int(input("Digite o comprimento do cômodo (SI): "))
    a = l*cp
    s+=a
    print("A área de {} é {} metros quadrados ".format(co, a))
    continuar = input("Deseja continuar? (SIM/NÃO) ")
    if continuar == "NÃO":
        print("A área total é: {} metros quadrados".format(s))
        break
