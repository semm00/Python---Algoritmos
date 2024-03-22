s = 0
contador = 0
while contador < 15:
    n = int(input(f"Digite o {contador+1}º número: "))
    f=1
    for c in range (1, n+1):
        f*=c
    s+=f
    contador += 1
print("O somatório do fatorial dos 15 números é {}".format(s))


