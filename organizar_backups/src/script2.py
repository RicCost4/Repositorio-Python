import calendar
import os
import datetime
import shutil
import re


def organizar_backups(subpasta):
    # Define a pasta que contém os backups a serem organizados
    pasta_backup = f'{os.getcwd()}/{subpasta}'
    # pasta_backup = f'/mnt/netapp01/{subpasta}'

    # Variavel que ira fazer a comparação do destino do arquivo
    condicao = False

    ## Define as pastas de destino para cada tipo de backup
    # Vemos que este diretório já existe.
    if not os.path.isdir('diarios'):  # se não, cria um.
        os.mkdir('diarios')
    backup_diarios = f'{pasta_backup}/diarios'

    # Vemos que este diretório já existe.
    if not os.path.isdir('semanais'):  # se não, cria um.
        os.mkdir('semanais')
    backup_semanais = f'{pasta_backup}/semanais'

    # Vemos que este diretório já existe.
    if not os.path.isdir('mensais'):  # se não, cria um.
        os.mkdir('mensais')
    backup_mensais = f'{pasta_backup}/mensais'

    # Define a expressão regular para extrair a data do nome do arquivo
    regex_data = r"\d{4}-\d{2}-\d{2}"  # Assume que a data está no formato "AAAA-MM-DD"
    # regex_data = r"\d{2}-\d{2}-\d{4}" # Assume que a data está no formato "DD-MM-AAAA"

    # Percorre todos os arquivos na pasta de backups
    for arquivo in os.listdir(pasta_backup):
        # Se não for um arquivo, passa para o próximo
        if not os.path.isfile(os.path.join(pasta_backup, arquivo)):
            continue

        # Extrai a data do nome do arquivo
        comparar = re.search(regex_data, arquivo)
        # Se o nome do arquivo não contiver uma data, passa para o próximo
        if not comparar:
            continue

        # Método que transforma a string em um objeto datetime
        data_backup = datetime.datetime.strptime(comparar.group(), "%Y-%m-%d")
        # data_backup = datetime.datetime.strptime(comparar.group(), "%d-%m-%Y")

        # Capturar a data atual.
        data_atual = datetime.datetime.now()

        # Calcula a diferença entre a data atual e a data do backup em dias
        diferenca_data = (data_atual - data_backup).days

        ## Condição que ira organizar os arquivos por diarias, semanais e mensais.
        # Condição diaria.
        if data_backup.month == data_atual.month:
            condicao = True
            pasta_destino = backup_diarios
        else:
            # Condição semanal.
            if data_backup.month != data_atual.month and diferenca_data <= 90:
                # Se for sexta-feira
                if data_backup.weekday() == 4:  # -> seg: 0, ter: 1, qua: 2, qui: 3, sex: 4, sab: 5, dom: 6.
                    condicao = True
                    pasta_destino = backup_semanais
                # Se o ultimo dia do mes

                if data_backup.day == calendar.monthrange(data_backup.year, data_backup.month)[1]:
                    condicao = True
                    pasta_destino = backup_mensais
                # Não é sexta-feira.
            # Condição mensal.
            else:
                if data_backup.day == calendar.monthrange(data_backup.year, data_backup.month)[1]:  # A função calendar.monthrange() já define anos bissextos.
                    condicao = True
                    pasta_destino = backup_mensais

        # Move o arquivo para a pasta de destino correspondente
        if condicao:
            shutil.move(os.path.join(pasta_backup, arquivo), os.path.join(pasta_destino, arquivo))
        else:
            os.remove(f'{pasta_backup}/{arquivo}')


if __name__ == "__main__":
    lista = ['teste1', 'teste2', 'teste3']

    for item in lista:
        organizar_backups(item)
