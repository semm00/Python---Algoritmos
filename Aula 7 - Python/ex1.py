lista = [1,2,3,4,5,6,7,8,9,10]
resp = 'sim'
while True:
    n = int(input("Digite um numero para buscar na lista: "))
    if n in lista:
        print(f"O número {n} está na lista!")
    else:
        print(f"O número {n} não está na lista!")
    resp = input("Deseja buscar outro número? [sim/não] ")
    if resp == 'não':
        break
print("Fim do programa!")
    