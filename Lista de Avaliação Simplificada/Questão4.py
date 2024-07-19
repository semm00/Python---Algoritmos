alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mensagem = input("Digite a mensagem a ser criptografada: ")
chave = int(input("Digite a chave de criptografia: "))
mensagem_criptografada = ""

for letra in mensagem:
    inicio = 0 
    fim=len(alfabeto)-1
    meio=(inicio+fim)//2
    while inicio<=fim and alfabeto[meio]!=letra:
        if letra<alfabeto[meio]:
            fim=meio-1
        else:
            inicio=meio+1
        meio=(inicio+fim)//2
        
    if alfabeto[meio]==letra:
        codigo = meio+chave
        if codigo > 25:
           codigo = codigo - 26
        mensagem_criptografada += alfabeto[codigo]
print("Mensagem criptografada:", mensagem_criptografada)