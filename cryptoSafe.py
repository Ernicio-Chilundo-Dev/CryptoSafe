import os
from cryptography.fernet import Fernet
import getpass

# Funcao para gerar chave de criptografia e salva-la em um arquivo

def gerar_chave():
    chave = Fernet.generate.key()
    with open("chave.key","wb") as chave_file:
        chave_file.write(chave)
        
        
# Funcao para carregar cheve do arquivo
def carregar_chave():
    return open("chave.key","rb").read()


# Funcao para criptografar aquivo
def criptografar_arquivo(nome_arquivo,chave):
    fernet = Fernet(chave)
    with open(nome_arquivo,"rb") as file:
        dados = file.read()
    dados_criptados = fernet.encrypt(dados)
    with open(nome_arquivo, "wb") as file:
        file.write(dados_criptados)
        

# Funcao para descriptografar arquivo
def descriptografar_arquivo(nome_arquivo,chave):
    fernet = Fernet(chave)
    with open(nome_arquivo,"rb") as file:
        dados_criptados = file.read()
    dados = fernet.decrypt(dados_criptados)
    with open(nome_arquivo,"wb") as file:
        file.write(dados)
        
# Funcao para configurar pasta segura

def criar_pasta_segura():
    pasta = "Pasta_Segura"
    os.makedirs(pasta,exist_ok=True)
    gerar_chave()
    print("Pasta segura criada com sucesso!")
    
    
# Funcao para adicionar um arquivo a pasta segura e criptografa-la
def adicionar_arquivo(nome_arquivo):
    chave = carregar_chave()
    criptografar_arquivo(nome_arquivo,chave)
    os.replace(nome_arquivo, os.path.join("Pasta_Segura",nome_arquivo))
    print(f"Arquivo {nome_arquivo} criptografado e movido para pasta segura")
    
    
# Funcao para acessar um arquivo na pasta segura e descriptografa-lo
def acessar_arquivo(nome_arquivo):
    chave = carregar_chave()
    caminho_arquivo = os.path.join("Pasta_Segura",nome_arquivo)
    if os.path.exists(caminho_arquivo):
        senha = getpass.getpass("Digite a senha para acessar o arquivo: ")
        if senha == "12345678":
            descriptografar_arquivo(caminho_arquivo,chave)
            print(f"Arquivo {nome_arquivo} descriptografado e pronto para o uso")
        else:
            print("Senha incorreta. Acesso negado")
    else:
        print("Arquivo nao encontrado na pasta segura!")
        
# Funcao menu, funcao principal porque vai gerenciar todas as outras funcoes do programa
def menu():
    print("====Pasta Segura====")
    print("1. Criar pasta segura")
    print("2. Adicionar arquivo na pasta segura")
    print("3. Acessar arquivo na pasta segura")
    print("4. Sair")
    
    while True:
        escolha = input("Digite a sua escolha:")
        if escolha == "1":
            criar_pasta_segura()
        elif escolha == "2":
            nome_arquivo = input("Digite o nome do arquivo para adicionar: ")
            adicionar_arquivo(nome_arquivo)
        elif escolha == "3":
            nome_arquivo = input("Digite o nome do arquivo para acessar")
            acessar_arquivo(nome_arquivo)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opcao invalida. Tente novamete")
            
menu()