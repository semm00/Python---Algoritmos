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

for j in range(len(list_pl)):
    if list_pl[j] == maior:
        print(f"O dia que mais choveu foi o {j+1}° dia")
        break 
for k in range(len(list_pl)):
    if list_pl[k] == menor:
        print(f"O dia que menos choveu foi o {k+1}° dia")
        break  
        
print(f"A média pluviométrica da primeira quinzena é {s1/15} %")
print(f"A média pluviométrica da segunda quinzena é {s2/15} %")
