soma = 0
contador = 0
m = 0
while contador < 10:
    n = int(input(f"Digite o {contador+1}º número: "))
    soma += n
    m = soma/10
    i=1
    contador += 1
print("A média é {} e o somatório dos valores é {}".format(m, soma))
    
    