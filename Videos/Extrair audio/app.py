import moviepy.editor

# Carrega arquivo do video
nome = input("carregar video: ")
arq_video = nome+".mp4"
video = moviepy.editor.VideoFileClip(arq_video)

# Extrai apenas o audio do video
audio_data = video.audio

# salva o arquivo de audio extraido do video
arq_audio = nome+".mp3"
audio_data.write_audiofile(arq_audio)