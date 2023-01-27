import os

caminhoAtual = os.getcwd()  # ler o caminho atual sendo executado o programa
venv = "python -m venv venv"
activate = './venv/Scripts/Activate.ps1'
flags = os.O_RDWR | os.O_CREAT

print(caminhoAtual)
nomePasta = input('nome da pasta: ')
if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe
    print('Ja existe uma pasta com esse nome!')
else:  # se não, cria um
    os.mkdir(nomePasta)
    os.mkdir(f'{nomePasta}/src')
    criarArquivo = os.open(f'./{nomePasta}/main.py', flags)
    str = """
    # Abrir terminal do editor e escrever os seguinte comandos:
    #    1. {venv} - ele ira criar o ambiente virtual do seu projeto,
    #    2. {activate} - ele ira ativar o ambiente virtual do seu projeto.
    """
    os.write(criarArquivo, str.encode())
    os.lseek(criarArquivo, 0, 0)

print("Projeto criado com Sucesso")
