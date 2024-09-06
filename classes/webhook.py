from discord_webhook import DiscordWebhook
from classes.colors import bcolors


def post_webhook(msg, url):
    webhook = DiscordWebhook(url=url, content=msg)
    try:
        response = webhook.execute()
        if response.status_code == 200:
            print(bcolors.GREEN_WARN + 'Webhook enviado com sucesso!')
        else:
            print(bcolors.RED_WARN + f'Falha ao enviar a webhook. Código de status: {response.status_code}')
    except Exception as err:
        print(bcolors.RED_WARN + 'Erro ao enviar a webhook' + bcolors.ENDC + '\nErro: ' + bcolors.FAIL + str(err) + bcolors.ENDC)
