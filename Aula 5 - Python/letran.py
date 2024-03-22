s=0
m=0
c=0
n=1
while n > 0:
    n=int(input("Digite um valor: "))
    if n>0:
        s+=n
        c+=1
        m=s/c
print("O somatorio é {}, a média é {} e foram {} valores lidos no total".format(s, m, c))