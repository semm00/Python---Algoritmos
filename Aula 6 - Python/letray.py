a = []
for i in range(15):
    n = (int(input("Digite um número inteiro: ")))
    a.append(n)
    
tp = 0
for n in a:
    if n % 2 == 0:
        tp += 1
print("O total de elementos pares na matriz é:", tp)