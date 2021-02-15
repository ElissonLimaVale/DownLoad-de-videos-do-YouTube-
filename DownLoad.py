import string
from pytube import YouTube as getTube
import moviepy.editor as mp
import re
import os

if not os.path.isdir("YouTubeArchives"):
    os.mkdir("YouTubeArchives")

path = "YouTubeArchives"
#função que converte o arquivo para o tipo passado
def Convert(type, path):
    print("CONVERTENDO ARQUIVO PARA " + type + "....")
    for file in os.listdir(path):
        if re.search("map4", file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + type)
            if type == ".mp3":
                new_file = mp.AudioFileClip(mp4_path)
                new_file.Write_audiofile(mp3_path)
                os.remove(mp4_path)

#fim do metod de conversão

#função para fazer o download
def downloader(link):

    tube = getTube(link)
    type = input("Qual tipo de arquivo V(video) / A(audio), V/A?: ")

    print("BAIXANDO ARQUIVO ....")
    if type.upper() == "A":
        archive = tube.streams.filter(only_audio=True).first().download(path)
        print("arquivo: " + tube.title)
        Convert(".mp3", path)
    else:
        archive = tube.streams.get_highest_resolution()
        archive.download(path)

    print("DOWNLOAD FINALIZADO!")
#fim da função de download

link = "S"

while link.upper != "N":
    link = input("Cole o link do Youtube: ")
    downloader(link)
    link = input("Deseja fazer mas downloads? S/N: ")

print("PROGRAMA FINALIZADO!")
