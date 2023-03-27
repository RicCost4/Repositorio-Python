import os

while (True):
    nomePasta = input("caminho da pasta: ")

    if os.path.isdir(nomePasta):  # vemos de este diretorio ja existe.
        os.chdir(f'{nomePasta}')
        os.system('docker-compose -f docker-compose.yml build')
        os.system('docker-compose -f docker-compose.yml up -d')
    else:  # se não, encerra.
        print('Não existe uma pasta com esse nome!\nTente novamente!!')
        break

    opc = input("deseja subir mais? (S/N)")
    if opc == 'N' or opc == 'n':
        print('Programa Encerrado!!')
        break
