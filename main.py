from classes.ytvideos import find_musicas_em_alta
from classes.webhook import post_webhook
from classes.heartArt import desenhar_coracao
from classes.colors import bcolors
import os, json





with open(os.path.join('data', 'config.json')) as data:
    json_data = json.load(data)

Discord_Webhook_URL = json_data['WEBHOOK']
Send_Webhook = json_data['SEND_WEBHOOK']

def iniciar():
    videos = find_musicas_em_alta('BR', 5)
    if videos:
        for video_title, video_id, video_views in videos:
            print(f"{bcolors.CYAN_WARN} Música em alta encontrada!\n        Nome: {video_title} \n        ID: {video_id} \n        Visus: {video_views}")
    else:
        print(f"{bcolors.RED_WARN} Nenhuma música encontrada ou o envio de webhook está desabilitado.")



def main():
    desenhar_coracao(80, 15, "", "M")
    print(f"")
    iniciar()


# post_webhook(mensagem, Discord_Webhook_URL)

if __name__ == "__main__":
    main()

