s1=0
s2=0
list_pl = []
for i in range (1,31):
    pl = int (input("Digite o {}° numero: ".format(i)))
    if i <= 15:
        s1+=pl
    else:
        s2+=pl
    list_pl.append(pl)
    maior = list_pl[0]
    menor = list_pl[0]
    for n in list_pl:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print("O dia que mais choveu foi o {}° dia".format(list_pl.index(maior)+1))
print("O dia que menos choveu foi o {}° dia".format(list_pl.index(menor)+1))        
print("A média pluviométrica da primeira quinzena é {}%: ".format(s1/15))
print("A média pluviométrica da segunda quinzena é {}%: ".format (s2/15))
