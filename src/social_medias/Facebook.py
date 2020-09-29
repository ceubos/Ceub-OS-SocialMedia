from dotenv import load_dotenv
from pyfacebook import Api
import os
import requests


class Facebook:
    app_access_token = None
    pages = []

    def __init__(self):
        credentials = self.getCredentials()
        if credentials is False:
            raise Exception(
                "A credências não estão configuradas corretamente, verifique os valores do .env: FACEBOOK_API_KEY, FACEBOOK_API_SECRET"
            )

    def getCredentials(self):
        """
        Obtém credênciais de um App Facebook.
        Retorna um Dict com as credênciais se estiverem definidas.
        :return: Dict | False
        """
        load_dotenv()
        appId = os.getenv('FACEBOOK_APP_ID')
        appSecret = os.getenv('FACEBOOK_APP_SECRET')
        if appId and appSecret:
            return {
                'app_id': appId,
                'app_secret': appSecret
            }
        return False

    def get_app_access_token(self):
        """
        Obtém credênciais do usuário.
        return: String | None
        """
        credentials = self.getCredentials()
        response = requests.get(
            url='https://graph.facebook.com/oauth/access_token',
            params={
                'client_id': credentials['app_id'],
                'client_secret': credentials['app_secret'],
                'grant_type': 'client_credentials'
            }
        )

        tokenObject = response.json()
        if self.app_access_token is None:
            if 'access_token' in tokenObject:
                self.app_access_token = tokenObject['access_token']
        return self.app_access_token

    def get_page_access_token(self, fb_page_id):

        response = requests.get(
            url='https://graph.facebook.com/' + str(fb_page_id),
            params={
                'fields': ['access_token'],
                'access_token': self.get_app_access_token()
            }
        )
        tokenObject = response.json()
        teste = 1

    def createPagePost(self, text):
        self.api.get_long_token('')
