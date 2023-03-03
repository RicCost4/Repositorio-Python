import os
from datetime import datetime
import shutil

# Funções
def pastaAno(destiny, ano):
    if os.path.isdir(f'{destiny}/{ano}'):  # vemos de este diretorio ja existe.
        return
    else:  # se não, cria um.
        print('criando pasta...')
        os.mkdir(f'{destiny}/{ano}')
        print(f'Pasta ./{ano} criado com sucesso!!\n')

def pastaMes(destiny, ano, mes):
    if os.path.isdir(f'{destiny}/{ano}/{mes}'):  # vemos de este diretorio ja existe.
        return
    else:  # se não, cria um.
        print('criando pasta...')
        os.mkdir(f'{destiny}/{ano}/{mes}')
        print(f'Pasta ./{mes} criado com sucesso!!\n')

def transferir(origin, destiny, ano, mes, file):
    # Concatena o caminho completo do arquivo de origem
    origin_path = f'{origin}/{file}' 
    # Concatena o caminho completo do arquivo de destino
    concatenated_path = f'{destiny}/{ano}/{mes}'
    path_destination = f'{concatenated_path}/{file}'
    # Move o arquivo da pasta origem para a pasta destino
    shutil.move(origin_path, path_destination)
    print(f'{file} transferido com sucesso.')

# diretório das imagens
dir_path_origin = input('Caminho da pasta? ')
# Selecionado a pasta que vai receber os arquivos.
dir_path_destiny = input('Caminho da pasta para transferencia? ')
# verificando se a data de criação é no ano desejados
ano = int(input('Ano Desejado: '))

# lista todos os arquivos do diretório
files = os.listdir(dir_path_origin)

# percorre todos os arquivos
for filename in files:
    # verifica se é um arquivo de imagem (PNG ou JPG ou JPEG)
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # obtendo a data de criação do arquivo
        data_criacao = datetime.fromtimestamp(os.path.getmtime(f'{dir_path_origin}/{filename}'))
        
        # verificando se a data de criação é no ano desejados
        if data_criacao.year == ano:
            pastaAno(dir_path_destiny, ano)
            # verificando e organizando por mes de cada ano.
            if data_criacao.month == 1:
                pastaMes(dir_path_destiny, ano, 'janeiro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'janeiro', filename)

            if data_criacao.month == 2:
                pastaMes(dir_path_destiny, ano, 'fevereiro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'fevereiro', filename)

            if data_criacao.month == 3:
                pastaMes(dir_path_destiny, ano, 'marco')
                transferir(dir_path_origin, dir_path_destiny, ano, 'marco', filename)

            if data_criacao.month == 4:
                pastaMes(dir_path_destiny, ano, 'abril')
                transferir(dir_path_origin, dir_path_destiny, ano, 'abril', filename)

            if data_criacao.month == 5:
                pastaMes(dir_path_destiny, ano, 'maio')
                transferir(dir_path_origin, dir_path_destiny, ano, 'maio', filename)

            if data_criacao.month == 6:
                pastaMes(dir_path_destiny, ano, 'junho')
                transferir(dir_path_origin, dir_path_destiny, ano, 'junho', filename)

            if data_criacao.month == 7:
                pastaMes(dir_path_destiny, ano, 'julho')
                transferir(dir_path_origin, dir_path_destiny, ano, 'julho', filename)

            if data_criacao.month == 8:
                pastaMes(dir_path_destiny, ano, 'agosto')
                transferir(dir_path_origin, dir_path_destiny, ano, 'agosto', filename)

            if data_criacao.month == 9:
                pastaMes(dir_path_destiny, ano, 'setembro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'setembro', filename)

            if data_criacao.month == 10:
                pastaMes(dir_path_destiny, ano, 'outubro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'outubro', filename)

            if data_criacao.month == 11:
                pastaMes(dir_path_destiny, ano, 'novembro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'novembro', filename)

            if data_criacao.month == 12:
                pastaMes(dir_path_destiny, ano, 'dezembro')
                transferir(dir_path_origin, dir_path_destiny, ano, 'dezembro', filename)