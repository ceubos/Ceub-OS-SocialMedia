from dotenv import load_dotenv
import os
import tweepy
from tweepy import TweepError


class Twitter:
    """
    Responsável por abstrair as chamadas de api para o Twitter.com.
    Utiliza OAUTH2 conforme descrito em: https://developer.twitter.com/en/docs/authentication/oauth-2-0
    :attribute api -> Representa objeto de Api do Tweepy
    """
    api = None
    base_url = 'https://api.twitter.com'

    def __init__(self):
        credentials = self.getCredentials()
        auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])
        auth.set_access_token(credentials['api_access_token'], credentials['api_access_token_secret'])
        self.api = tweepy.API(auth)

    def getCredentials(self):
        """
        Obtém credênciais do Twitter configuradas no .env
        Emite a excessão Exception caso esteja mal configurado ou indisponível.
        :return: Objeto Dict contendo as credênciais configuradas.
        """
        load_dotenv()
        apiKey = os.getenv('TWITTER_API_KEY')
        apiSecretKey = os.getenv('TWITTER_API_SECRET_KEY')
        apiAccessToken = os.getenv('TWITTER_API_ACCESS_TOKEN')
        apiAccessTokenSecret = os.getenv('TWITTER_API_ACCESS_TOKEN_SECRET')

        if apiKey and apiSecretKey and apiAccessToken and apiAccessTokenSecret:
            return {
                'api_key': apiKey,
                'api_secret_key': apiSecretKey,
                'api_access_token': apiAccessToken,
                'api_access_token_secret': apiAccessTokenSecret
            }
        raise Exception(
            "TWITTER_API_KEY ou TWITTER_API_SECRET_KEY não configurados. Execute configure.py para configura-los.")

    def getIsReady(self):
        """
        Verifica se está pronto para realizar operações no Twitter validando as credenciais incluídas.
        :return: True | False
        """
        try:
            api = self.api
            return api.verify_credentials()
        except Exception:
            return False
