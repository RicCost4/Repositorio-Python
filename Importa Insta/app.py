from datetime import datetime
from tqdm import tqdm
from tqdm import trange
import time
import os
import instaloader

def data_inicial():
    dia = int(input("Digite o dia inicial: "))
    mes = int(input("Digite o mes inicial: "))
    ano = int(input("Digite o ano inicial: "))

    return datetime(ano, mes, dia)


def data_final():
    dia = int(input("Digite o dia final: "))
    mes = int(input("Digite o mes final: "))
    ano = int(input("Digite o ano final: "))    
    
    return datetime(ano, mes, dia)

def post_conta(perfil, pasta):
    opcao = input('Deseja baixar posts da conta? (S/N)')
    if opcao == 's' or opcao == 'S':
        # percorre os post e baixa apenas os que estão dentro do periodo desejado
        profile = instaloader.Profile.from_username(L.context, perfil).get_posts()
        
        SINCE = data_inicial()
        UNTIL = data_final()
        os.system('cls')
        for post in profile:
            
            if (post.date >= SINCE) and (post.date <= UNTIL):
                print(post.date)
                L.download_post(post, pasta)
            for _ in trange(10, desc="..."):
                time.sleep(1)


def storys(perfil, pasta):
    opcao = input('Deseja baixar storys da conta? (S/N)')
    if opcao == 's' or opcao == 'S':
        # Percorra as histórias e baixe cada uma
        profile = instaloader.Profile.from_username(
            L.context, perfil).has_viewable_story()
        os.system('cls')
        for story in tqdm(profile, desc="baixando..."):
            L.download_story(story, pasta)

# carrega a lib e faz login com a conta desejada
L = instaloader.Instaloader(
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    filename_pattern='{profile}_{mediaid}'
)

# contas privadas precisa esta logado, essa função esta em construção e atualização.
print("Download de Post do instagram de contas publicas")
perfil = input("Perfil: ")

pasta = "insta-"+perfil

post_conta(perfil, pasta)
#Precisa esta logado
#storys(perfil, pasta)
