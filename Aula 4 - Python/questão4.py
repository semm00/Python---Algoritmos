#Valores
a=int(input("Digite o primeiro valor:"))
b=int(input("Digite o segundo valor:"))
c=int(input("Digite o terceiro valor:"))

#Distribuição e Troca de Valores 
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a, b, c)
