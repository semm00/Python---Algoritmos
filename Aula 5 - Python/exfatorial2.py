while True:
    n = int (input("Digite um valor: "))
    f = 1
    for c in range (1, n+1):
     f *= c 
    print(f)
    continuar = input("Deseja continuar? (s/n) ")
    if continuar == "n":
        break
