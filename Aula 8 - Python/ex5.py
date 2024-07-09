list = [12,3,11,5,1,9,7,15,13]
max = list[0]
for i in list[1:]:
    if i>max: #só inverter o sinal e ele vai imprimir o menor 
        max = i
print(max)