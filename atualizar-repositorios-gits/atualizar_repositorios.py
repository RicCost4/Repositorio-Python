import os
import time

def path(path_dir):
    os.chdir(path_dir)
    os.system('git pull')

with open('path_repositorios.txt', 'r') as f:
    linhas = f.readlines()

for linha in linhas:
    linha = linha.strip()
    path(linha)
    time.sleep(2)
    #print(linha)