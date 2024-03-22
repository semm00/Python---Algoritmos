vh= int(input('Coloque o valor que você ganha por hora: '))
nt= int(input('Coloque o número de horas que você trabalha: '))
inss= int(input('Coloque o percentual de desconto do INSS: '))
sb= vh*nt
sl= sb-(sb*inss/100)
print("Seu salário liquido é: ", sl)