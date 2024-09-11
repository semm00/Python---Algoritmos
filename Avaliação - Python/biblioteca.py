import codigofonte
from time import sleep

while True:
    def main():
        print("\n")
        print("Olá! Seja bem-vindo à biblioteca, cadastre-se para consultar nosso sistema.")
        print("\n")
        sleep(1)
        codigofonte.cadastro_usuario() 
        print("Cadastro realizado com sucesso!")
        sleep(1)
        print("\n")
        codigofonte.busca_livros()
    if __name__ == "__main__":
        main()
