from datetime import datetime
from tqdm import tqdm
from tqdm import trange
import instaloader
import time
import getpass

# função de login


def loading_user():
    user = input("Usuario: ")
    senha = getpass.getpass("Senha: ", stream=None)
    L.login(user, senha)
    for _ in trange(100, desc="Loading..."):
        time.sleep(0.25)
    print("Loading Done!")


def timeInicial():
    anoIni = int(input("Digite o ano inicial: "))
    mesIni = int(input("Digite o mes inicial: "))
    diaIni = int(input("Digite o dia inicial: "))
    SINCE = datetime(anoIni, mesIni, diaIni)
    return SINCE


def timeFinal():
    anoFim = int(input("Digite o ano final: "))
    mesFim = int(input("Digite o mes final: "))
    diaFim = int(input("Digite o dia final: "))
    UNTIL = datetime(anoFim, mesFim, diaFim)
    return UNTIL


# carrega a lib e faz login com a conta desejada
L = instaloader.Instaloader(
    download_pictures=True,
    download_videos=True,
    download_video_thumbnails=True,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    filename_pattern='{profile}_{mediaid}'
)
print("Download de Post do instagram*DESATIVAR A VERIFICAÇÃO EM DUAS ETAPAS*")
loading_user()


# carrega todos os post do perfil escolhido
perfil = input("Perfil: ")
posts = instaloader.Profile.from_username(
    L.context, perfil).get_posts()


inicial = timeInicial()
final = timeFinal()

# percorre os post e baixa apenas os que estão dentro do periodo desejado
pasta = "instadowload("+perfil+")"
for post in tqdm(posts, desc="baixando..."):
    time.sleep(0.5)
    if (post.date >= inicial) and (post.date <= final):
        print(post.date)
        L.download_post(post, pasta)
