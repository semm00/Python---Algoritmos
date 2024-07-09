lista = [1,2,3,4,5,6,7,8,9,10]
resp = 'sim'
while True:
    achou = False
    n = int(input("Digite um numero para buscar na lista: "))
    cont = 0
    while cont < len(lista):
        if lista[cont] == n:
            achou=True
            break
        cont += 1
    if achou:
        print(f"O número {n} foi encontrado na posição {cont+1} da lista!")
    else: 
        print(f"O número {n} não está na lista!")
    resp = input("Deseja buscar outro número? [sim/não] ")
    if resp == 'não':
        break
print("Fim do programa!")