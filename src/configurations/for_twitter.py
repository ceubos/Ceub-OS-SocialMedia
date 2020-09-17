from dotenv import load_dotenv
import src.console as console
import os
from src.social_medias.Twitter import Twitter

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
    twitterAccessToken = None
    twitterAccessSecret = None
    while twitterApiKey is None:
        twitterApiKey = console.getInput('TWITTER_API_KEY:')
    while twitterApiSecret is None:
        twitterApiSecret = console.getInput('TWITTER_API_SECRET:')
    while twitterAccessToken is None:
        twitterAccessToken = console.getInput('TWITTER_API_ACCESS_TOKEN')
    while twitterAccessSecret is None:
        twitterAccessSecret = console.getInput('TWITTER_API_ACCESS_TOKEN_SECRET')

    twitterApiKey = twitterApiKey.strip()
    twitterApiSecret = twitterApiSecret.strip()
    twitterAccessToken = twitterAccessToken.strip()
    twitterAccessSecret = twitterAccessSecret.strip()

    file.write('\nTWITTER_API_KEY=' + twitterApiKey)
    file.write('\nTWITTER_API_SECRET_KEY=' + twitterApiSecret)
    file.write('\nTWITTER_API_ACCESS_TOKEN=' + twitterAccessToken)
    file.write('\nTWITTER_API_ACCESS_TOKEN_SECRET=' + twitterAccessSecret)
    file.close()

    twitter = Twitter()
    if twitter.getIsReady():
        console.printSuccessLine("Twitter configurado com sucesso!")
        return True

    console.printLine("TWITTER_API_KEY ou TWITTER_API_SECRET inválidos.")
    return False
