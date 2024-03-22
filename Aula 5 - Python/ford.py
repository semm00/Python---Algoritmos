for c in range (1, 501):
    if c%2==0:
        somatorio=0
        for i in range(1, c+1):
            somatorio+=i
            i+=1
        print("O somatório do número: ", c,"é: ", somatorio)
print("FIM!")
        