#Notas do aluno
n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota:"))
n3=float(input("Digite a terceira nota:"))
n4=float(input("Digite a quarta nota:"))

media=(n1+n2+n3+n4)/4

if media>=7:
    print("Aprovado", media)
    
#Exame final e nova media
else: ef=float(input("Nota do Exame Final:"))
newmedia=(media+ef)/2
if newmedia>=5: 
    print("Aprovado no exame final", newmedia)
else: print("Reprovado", newmedia)
      
