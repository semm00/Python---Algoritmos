#Coeficientes
a=float(input("Digite o valor de a:"))
b=float(input("Digite o valor de b:"))
c=float(input("Digite o valor de c:"))

#Delta e Raízes
delta= b**2-4*a*c
x1 = (-b+delta**(1/2))/2*a
x2 = (-b-delta**(1/2))/2*a

#Condições de Delta
if delta>0:
    print(x1,x2, "Raízes são diferentes")
else: 
    if delta==0:
        print("Raízes são iguais", x1)
    else: print("Não há raízes reais")
    