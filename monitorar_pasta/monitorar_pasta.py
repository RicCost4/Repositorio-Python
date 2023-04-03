import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print('==================================')
        # print(event)
        print('Arquivo modificado:', event.src_path)
        print('')
        opc = input('Modificação encontrada, deseja fazer algo? (S/N): ')
        if opc.upper() == 'S':
            caminho_pai = os.path.abspath(os.path.dirname(event.src_path))
            print('Caminho do diretório pai:', caminho_pai)
            os.chdir(caminho_pai)
            os.system('git add .')
            commit = input('Mensagem do commit: ')
            os.system(f'git commit -m "{commit}"')
            pull = input('Deseja fazer o push? (S/N): ')
            if pull.upper() == 'S':
                os.system('git push')
        print('')

path = input('Digite o caminho absoluto da pasta: ')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
observer = Observer()
observer.schedule(MyHandler(), path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
