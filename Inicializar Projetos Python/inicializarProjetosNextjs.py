import os


def criar_projeto(diretorio, pasta, npx):
    print(f'criando ambiente do projeto...')
    os.chdir(f'{str(diretorio)}\{str(pasta)}')
    os.system(f'{str(npx)}')
    print(f'\nambiente criando com sucesso!!')


caminhoAtual = os.getcwd()
npx = 'npx create-next-app'

nomePasta = input("nome da pasta: ")
if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe
    print('Ja existe uma pasta com esse nome!\n')

    criar_projeto(caminhoAtual, nomePasta, npx)
else:  # se não, cria um
    print('criando pasta...\n')
    os.mkdir(nomePasta)
    print(f'./{nomePasta} criado com sucesso!!')

    criar_projeto(caminhoAtual, nomePasta, npx)
