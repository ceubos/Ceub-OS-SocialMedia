from dotenv import load_dotenv
import src.console as console
import os
from src.social_medias.TwitterApi import TwitterApi

load_dotenv()


def configureTwitter(file):
    """
    """
    twitterApiKey = None
    twitterApiSecret = None
    while twitterApiKey is None:
        twitterApiKey = console.getInput('TWITTER_API_KEY:')
    while twitterApiSecret is None:
        twitterApiSecret = console.getInput('TWITTER_API_SECRET:')
    twitterApiKey = twitterApiKey.strip()
    twitterApiSecret = twitterApiSecret.strip()

    file.writelines([
        'TWITTER_API_KEY=' + twitterApiKey,
        'TWITTER_API_SECRET=' + twitterApiSecret
    ])
    file.close()

    twitterApi = TwitterApi()
    if twitterApi.getIsReady():
        console.printSuccessLine("Twitter configurado com sucesso!")
        return True

    console.printLine("TWITTER_API_KEY ou TWITTER_API_SECRET inválidos.")
    return False
