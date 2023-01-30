import os
import time
from tqdm import trange

caminhoAtual = os.getcwd()
venv = 'python -m venv venv'
activate = '.\\venv\\Scripts\\Activate.bat'
flags = os.O_RDWR | os.O_CREAT

nomePasta = input("nome da pasta: ")
if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe
    print('Ja existe uma pasta com esse nome!')
else:  # se não, cria um
    print('criando pasta...')
    os.mkdir(nomePasta)
    for _ in trange(40, desc="Criando..."):
        time.sleep(0.1)
    print(f'./{nomePasta} criado com sucesso!!')

    print(f'criando subdiretorio /{nomePasta}/src ...')
    os.mkdir(f'{nomePasta}/src')
    for _ in trange(40, desc="Criando..."):
        time.sleep(0.1)
    print(f'subdiretorio /{nomePasta}/src criando com sucesso!!')

    print(f'criando arquivo /{nomePasta}/main.py ...')
    criarArquivo = os.open(f'./{nomePasta}/main.py', flags)
    str = """
    # Abrir terminal do editor e escrever o seguinte comando:
    #    2. {activate} - ele ira ativar o ambiente virtual do seu projeto.
    """
    os.write(criarArquivo, str.encode())
    os.lseek(criarArquivo, 0, 0)
    os.close(criarArquivo)
    for _ in trange(50, desc="Criando..."):
        time.sleep(0.2)
    print(f'arquivo /{nomePasta}/main.py criando com sucesso!!')

    print(f'criando ambiente virtual do projeto...')
    os.chdir(f'{caminhoAtual}\{nomePasta}')
    os.system(f'{venv}')
    for _ in trange(80, desc="baixando..."):
        time.sleep(0.25)
    print(f'ambiente virtual do criando com sucesso!!')

    # opcao = input('Deseja instalar bibliotecas juntos?(S/N): ')
    # if opcao.lower() == 's':
    #     try:
    #         os.system(f'{activate}')
    #         while True:
    #             strPip = input('Digite o import: ')
    #             # pip install pillow, pip install opencv-python, pip install pyautogui
    #             if strPip == '':
    #                 print('Linha invalida, digite novamente!!')
    #             else:
    #                 try:
    #                     os.system(f'{strPip}')
    #                 except TypeError:
    #                     print(TypeError)

    #             continuar = input('Deseja intalar mais bibliotecas?(S/N): ')
    #             if continuar.lower() != 's':
    #                 break
    #     except TypeError:
    #         print(TypeError)

print("Projeto criado com Sucesso")
