cpf=input("Digite o cpf: ")
primeiro_digito=0
segundo_digito=0
soma=0
soma2=0
#calculando o primeiro digito
for cont in range(10,1,-1):
    numero=cpf[10-cont]
    soma+=int(numero)*cont
    
if soma%11<2:
    primeiro_digito=0
else:
    primeiro_digito=11-(soma%11)

#calculando o segundo digito
for cont in range(11,1,-1):
    numero=cpf[11-cont]
    soma2+=int(numero)*cont
    
if soma2%11<2:
    segundo_digito=0
else:
    segundo_digito=11-(soma2%11)

#verificando se o cpf é valido
if cpf[-2]==str(primeiro_digito) and cpf[-1]==str(segundo_digito):
    print("CPF valido")
else:
    print("CPF invalido")