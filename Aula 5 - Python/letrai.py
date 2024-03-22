a, b = 1, 1
c = 0
while c < 15:
    print(a, end=" ") #end serve para colocar os elemento em linha
    # Calcula o próximo número da sequência
    proxn = a+b
    a = b
    b = proxn
    c += 1
    #1, 1 = 1, 1 + 1
    #1, 2 = 2, 2 + 1
    #2, 3 = 3, 3 + 2
    #a, b = b, a + b tbm funciona
    