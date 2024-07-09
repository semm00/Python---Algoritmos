a = [[0 for j in range(5)] for i in range(4)]
b = [[0 for j in range(5)] for i in range(4)]
c = [[0 for j in range(5)] for i in range(4)]
for i in range (4):
    for j in range(5):
        while a[i][j] == 0:
            n = int(input("Digite um numero para adiciona-lo a matriz a: "))
            if n % 12 == 0:
                a[i][j] = n
            else:
                print("Digite um número divisível por 3 e 4!")
            
for i in range (4):
    for j in range(5):
        while b[i][j] == 0:
            n2 = int(input("Digite um numero para adiciona-lo a matriz b: "))
            if n2%5 == 0 or n2%6 == 0:
                b[i][j] = n2
            else:
                print("Digite um número divisível por 5 ou 6!")
                
for i in range (4):
    for j in range(5):
        c[i][j] = a[i][j] - b[i][j]
            
for linha in a:
    print(linha)

for linha in b:
    print(linha)
    
for linha in c:
    print(linha)