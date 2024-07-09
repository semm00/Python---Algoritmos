a = []
impar = 0
total = 0
for i in range (10):
    a.append(int(input(f"Digite o {i+1}° numero: ")))
    if a[i] % 2 != 0:
        impar+=1
    total+=1
print(f"Quantidade de numeros impares: {impar}")
print(f"Porcentagem de numeros impares: {impar/total*100}%")