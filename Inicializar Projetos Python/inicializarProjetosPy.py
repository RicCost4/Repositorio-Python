import os

caminhoAtual = os.getcwd()
venv = 'python -m venv venv'
activate = '.\\venv\\Scripts\\Activate.bat'
flags = os.O_RDWR | os.O_CREAT

nomePasta = input("nome da pasta: ")
if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe
    print('Ja existe uma pasta com esse nome!')
else:  # se não, cria um
    os.mkdir(nomePasta)
    print()
    os.mkdir(f'{nomePasta}/src')
    criarArquivo = os.open(f'./{nomePasta}/main.py', flags)
    str = """
    # Abrir terminal do editor e escrever o seguinte comando:
    #    2. {activate} - ele ira ativar o ambiente virtual do seu projeto.
    """
    os.write(criarArquivo, str.encode())
    os.lseek(criarArquivo, 0, 0)
    os.close(criarArquivo)

    os.chdir(f'{caminhoAtual}\{nomePasta}')
    os.system(f'{venv}')
    opcao = input('Deseja instalar bibliotecas juntos?(S/N): ')
    if opcao.lower() == 's':
        os.system(f'{activate}')
        while True:
            strPip = input('Digite o import: ')
            # pip install pillow, pip install opencv-python, pip install pyautogui
            if strPip == '':
                print('Linha invalida, digite novamente!!')
            else:
                try:
                    os.system(f'{strPip}')
                except TypeError:
                    print(TypeError)

            continuar = input('Deseja intalar mais bibliotecas?(S/N): ')
            if continuar.lower() != 's':
                break

print("Projeto criado com Sucesso")
