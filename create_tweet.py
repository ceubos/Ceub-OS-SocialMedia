from src.social_medias.Twitter import Twitter
import src.console as c
import json
import argparse

"""
Script para criar tweets.
Manual
    Para execúta-lo rode o seguinte comando:
        $ python create_tweet [TEXTO DO TWEET]
"""

twitter = Twitter()
if twitter.getIsReady() is False:
    c.printLine(
        "Você precisa configurar suas credenciais do Twitter primeiro, para isto execute: python configure.py ou defina os dotenvs necessários.")
else:
    parser = argparse.ArgumentParser(usage='python create_tweet.py [TEXTO_DO_TWEET]')
    parser.add_argument('tweet', help='Texto do tweet.')
    args = parser.parse_args()

    tweetText = args.tweet

    if len(tweetText) > 280:
        c.printErrorLine("Texto do tweet muito longo.")
        exit()

    c.printLine('Criando tweet: ' + tweetText)
    try:
        twitter.api.update_status(status=tweetText)
        c.printLine('Tweet criado!')
    except TweepError:
        c.printLine('Não foi possível criar este tweet.')
