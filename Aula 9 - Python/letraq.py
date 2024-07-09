import random
a = [[random.randint(1, 10) for j in range(5)] for i in range(4)]
b = []
c = []
for i in range(4):
    sla = 0
    for j in range(5):
        for k in range(0,a[i][j]+1):
            sla+=k
    b.append(sla)

for j in range(5):
    sca = 0
    for i in range(4):
        for k in range(0,a[i][j]+1):
            sca+=k
    c.append(sca)
smtb=0
for i in range(4):
    smb=0
    for k in range(0,b[i]):
        smb+=k
    smtb+=smb
        
    
smtc=0
for j in range(5):
    smc=0
    for k in range(0,c[j]):
        smc+=k
    smtc+=smc
    
for linha in a:
    print(linha)    
print("essa é a matriz b:", b)
print("esse é o total do somatório dos elementos da matriz b:", smtb)
print("essa é a matriz c:", c)
print("esse é o total da soma dos elementos da matriz c:", smtc)
