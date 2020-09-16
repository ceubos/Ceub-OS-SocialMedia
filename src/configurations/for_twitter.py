from dotenv import load_dotenv
import src.console as console
import os
from src.social_medias.TwitterApi import TwitterApi

load_dotenv()


def configureTwitter(file):
    """
    Configura automaticamente as váriaveis do Twitter no .env adequado.
    Váriaveis adequadas
    - TWITTER_API_KEY
    - TWITTER_API_SECRET
    """
    twitterApiKey = None
    twitterApiSecret = None
    while twitterApiKey is None:
        twitterApiKey = console.getInput('TWITTER_API_KEY:')
    while twitterApiSecret is None:
        twitterApiSecret = console.getInput('TWITTER_API_SECRET:')
    twitterApiKey = twitterApiKey.strip()
    twitterApiSecret = twitterApiSecret.strip()


    file.write('\nTWITTER_API_KEY=' + twitterApiKey)
    file.write('\nTWITTER_API_SECRET_KEY=' + twitterApiSecret)
    file.close()

    twitterApi = TwitterApi()
    if twitterApi.getIsReady():
        console.printSuccessLine("Twitter configurado com sucesso!")
        return True

    console.printLine("TWITTER_API_KEY ou TWITTER_API_SECRET inválidos.")
    return False
