lista = []
sm = 0
for i in range(20):
    ns = int(input("Digite o {}° número: ".format(i+1)))
    lista.append(ns)
    sm+=ns
x = lista[0]
for j in range(0, len(lista)):
    if lista[j] == lista[j-1]:
        x = lista[j]
        for k in range(len(lista)-1):
            for l in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
            
print("a moda dos números é: ", x)
print("a média dos números é: ", sm/20)
print("a mediana dos números é: ", (lista[9]+lista[10])/2)