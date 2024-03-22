#Notas do aluno
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
n3=float(input("Digite a terceira nota:"))
n4=float(input("Digite a quarta nota:"))

media=(n1+n2+n3+n4)/4

#Resultado
if media > 7:
    print("aprovado", media)
else:
 print("reprovado", media)
