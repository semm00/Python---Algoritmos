c = 1 #2,4,6,8,10,..,500
while c <= 500:
    if c%2==0:
        i=1
        s=0
        while i<=c:
            s+=i
            i+=1
        print("O somatório do número: ", c, "é: ", s)         
    c+=1
print("FIM!!")

        