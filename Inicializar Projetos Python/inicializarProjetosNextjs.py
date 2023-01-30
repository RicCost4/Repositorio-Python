import os

caminhoAtual = os.getcwd()
npx = 'npx create-next-app'

nomePasta = input("nome da pasta: ")
if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe
    print('Ja existe uma pasta com esse nome!\n')
    print('--------------------------------\n')
    print(f'criando ambiente do projeto...')
    os.chdir(f'{caminhoAtual}\{nomePasta}')
    os.system(f'{npx}')
    print(f'\nambiente criando com sucesso!!')
else:  # se não, cria um
    print('criando pasta...\n')
    os.mkdir(nomePasta)
    print(f'./{nomePasta} criado com sucesso!!')

    print(f'criando ambiente do projeto...')
    os.chdir(f'{caminhoAtual}\{nomePasta}')
    os.system(f'{npx}')
    print(f'\nambiente criando com sucesso!!')
