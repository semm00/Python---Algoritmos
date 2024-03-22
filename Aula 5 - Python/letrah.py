while True:
    b = int(input("Digite a base: "))
    e = int(input("Digite o expoente: "))
    if b >=0 and e >=0:   
        print("{}^{} = {}".format(b, e, b**e))
    else:
        break
print("FIM!")
        
