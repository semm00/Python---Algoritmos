n = int(input("Digite um número: "))
lista = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lista.append(i)
print(lista)