from time import sleep
import random

def cadastro_usuario():
    lista = []
    n = input('Digite seu nome: ')
    try:
        t = int(input('Digite seu telefone: '))
    except ValueError:
        print('Número inválido, digite apenas números!')
        t = int(input('Digite seu telefone: '))
    while True:
        if len(str(t)) != 11:
            print('Número inválido')
            t = int(input('Digite seu telefone: '))   
        else:
            break   
    em = input('Digite seu email: ')
    while True:
        if '@' not in em:
            print('Email inválido')
            em = input('Digite seu email: ')
        else:
            break
    cpf = input('Digite seu cpf: ')
    def validar_cpf(cpf):
        if len(cpf)!=11:
            print("CPF inválido")
            cpf = input('Digite um cpf válido: ')
            validar_cpf(cpf)
        else:
            primeiro_digito=0
            segundo_digito=0
            soma=0
            soma2=0
                
            #calculando o primeiro digito
            for cont in range(10,1,-1):
                numero=cpf[10-cont]
                soma+=int(numero)*cont
                    
            if soma%11<2:
                primeiro_digito=0
            else:
                primeiro_digito=11-(soma%11)

            #calculando o segundo digito
            for cont in range(11,1,-1):
                numero=cpf[11-cont]
                soma2+=int(numero)*cont
                    
            if soma2%11<2:
                segundo_digito=0
            else:
                segundo_digito=11-(soma2%11)

            #verificando se o cpf é valido
            if cpf[-2]!=str(primeiro_digito) or cpf[-1]!=str(segundo_digito):
                print("CPF inválido")
                cpf = input('Digite um cpf válido: ')
                validar_cpf(cpf)
                    
            else:
                return cpf    
    validar_cpf(cpf)  
             
    dados = {'nome': n, 'telefone': t, 'email': em, 'cpf': cpf}
    lista.append(dados)
    return lista

livros=[]
revistas = []
for i in range(random.randint(1,5)):
    livros.append("1984")
    
for i in range(random.randint(1,5)):
    livros.append("o caso dos 10 negrinhos")

for i in range(random.randint(1,5)):
    livros.append("o cortiço")
    
for j in range(random.randint(1,5)):
    revistas.append("vogue")
    
for i in range(random.randint(1,5)):
    revistas.append("forbes")
    
for i in range(random.randint(1,5)):
    revistas.append("caras")

def busca_livros():
    q = 0
    global livros
    global revistas
    lour = input("Você deseja buscar um livro ou uma revista (Digite livro ou revista)? ").lower()
    print("\n")
    if lour == "livro":
        busca = input("Digite o nome do livro que deseja buscar: ").lower()
        print("Carregando...")
        sleep(1)
        print("\n")
        if busca not in livros:
            print("Livro não encontrado!")
            print("\n")    
            busca2 = input("Deseja buscar de novo (Digite sim ou não)? ").lower()
            print("Carregando...")
            sleep(1) 
            print("\n")
            if busca2 == "sim":
                busca_livros()
            elif busca2 == "não":
                print("Até mais!")
                print("\n")
            else:
                print("Opção inválida")
                print("\n")
                busca_livros()
        else: 
            for j in range(len(livros)):
                if busca == livros[j]:
                    q+=1
            print("Livro encontrado!")
            print(f"A quantidade de exemplares do livro {busca} é {q}.") 
                
            
            print("\n")
            emprestar = input("Deseja pegar esse livro emprestado? (Digite sim ou não) ").lower() 
            print("\n")
            if emprestar == "sim":
                try:
                    data = int(input("Digite o dia de hoje (Digite 1,2,3,...,31): "))
                    while True:
                        if data < 1 or data > 31:
                            print("Data inválida, digite apenas números de 1 a 31!")
                            data = int(input("Digite o dia de hoje (Digite 1,2,3,...,31): "))
                        else:
                            break
                    print("Carregando...")
                    sleep(1) 
                except ValueError:
                    print("Data inválido, digite apenas números!")
                    data = int(input("Digite o dia de hoje (Digite 1,2,3,...,31): "))
                if data <= 23:
                    devolucao = data + 7
                    print(f"O livro deve ser devolvido até o dia {devolucao}.") 
                else:
                    devolucao = data - 23
                    print(f"O livro deve ser devolvido até o dia {devolucao} do próximo mês.") 
                print("\n")
                print("Livro emprestado com sucesso! Boa leitura!")
                livros.remove(busca)
            elif emprestar == "não":
                print("Até mais!")
                print("\n")
            else:
                print("Opção inválida")
                print("\n")
                busca_livros()
            
                
    elif lour == "revista":
        print("\n")
        busca = input("Digite o nome da revista que deseja buscar: ").lower()
        print("Carregando...")
        sleep(1)
        if busca not in revistas:
            print("\n")
            print("Revista não encontrada") 
            busca2 = input("Deseja buscar outra revista ou livro (Digite sim ou não)? ").lower()
            print("Carregando...")
            sleep(1) 
            print("\n")
            if busca2 == "sim":
                busca_livros()
            elif busca2 == "não":
                print("Até mais!")
                print("\n")
            else:
                print("Opção inválida")
                print("\n")
                busca_livros()
        else:
            for j in range(len(revistas)):
                if busca == revistas[j]:
                    q+=1
            print("Revista encontrada!")
            print(f"A quantidade de exemplares da revista {busca} é {q}.") 
            print("\n")
            emprestar = input("Deseja pegar essa revista emprestada (Digite sim ou não)? ").lower() 
            if emprestar == "sim":
                try:
                    data = int(input("Digite o dia de hoje (Digite 1,2,3,...,31): "))
                    while True:
                        if data < 1 or data > 31:
                            print("Data inválida, digite apenas números de 1 a 31!")
                            data = int(input("Digite o dia de hoje (Digite 1,2,3,...,31): "))
                        else:
                            break
                    print("Carregando...")
                    sleep(1)  
                except:
                    print("Data inválido, digite apenas números!")
                    data = int(input("Digite a data de hoje (Digite 1,2,3,...,31): "))
                if data <= 23:
                    devolucao = data + 7
                else:
                    devolucao = data - 23
                print(f"A revista deve ser devolvida até o dia {devolucao}.")  
                print("Revista emprestada com sucesso! Boa leitura! ")
                revistas.remove(busca)
            elif emprestar == "não":
                print("Até mais!")
                print("\n")
            else:
                print("Opção inválida")
                print("\n")
                busca_livros()
                
    else:
        print("Opção inválida")
        print("\n")
        busca_livros()
 
