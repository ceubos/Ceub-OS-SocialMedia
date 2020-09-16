from dotenv import load_dotenv
import os
import requests


class TwitterApi(object):
    """
    Responsável por abstrair as chamadas de api para o Twitter.com.
    Utiliza OAUTH2 conforme descrito em: https://developer.twitter.com/en/docs/authentication/oauth-2-0
    """
    previous_access_token = None
    base_url = 'https://api.twitter.com'

    def __init__(self):
        pass

    def getCredentials(self):
        """
        Obtém credênciais do Twitter configuradas no .env
        Emite a excessão Exception caso esteja mal configurado ou indisponível.
        :return: Objeto Dict contendo as credênciais configuradas.
        """
        load_dotenv()
        apiKey = os.getenv('TWITTER_API_KEY')
        apiSecretKey = os.getenv('TWITTER_API_SECRET_KEY')
        if apiKey and apiSecretKey:
            return {'api_key': apiKey, 'api_secret_key': apiSecretKey}
        raise Exception(
            "TWITTER_API_KEY ou TWITTER_API_SECRET_KEY não configurados. Execute configure.py para configura-los.")

    def getAccessToken(self, use_previous_access_token=True):
        """
        Obtém access_token
        Caso usePreviousAccessToken seja. True então é usada uma técnica de cache do access_token evitando realizar requests demasiados.
        https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens
        :return: String
        """
        if use_previous_access_token and self.previous_access_token is not None:
            return self.previous_access_token
        else:
            url = self.base_url + '/oauth2/token'
            credentials = self.getCredentials()
            response = requests.post(url, auth=(credentials['api_key'], credentials['api_secret_key']),
                                     data={'grant_type': 'client_credentials'})

            if response.status_code is 200:
                responseData = response.json()
                if "access_token" in responseData:
                    self.previous_access_token = responseData['access_token']
                    return responseData['access_token']
        raise Exception(
            "Não foi possível obter o access_token para as credênciais do Twitter cadastradas, talvez estejam erradas.")

    def getIsReady(self):
        """
        Obtém se a Api está configurada e pronta para uso.
        :return: True | False
        """
        try:
            self.getAccessToken(use_previous_access_token=True)
            return True
        except:
            return False

    """
    curl -XPOST 
      --url 'https://api.twitter.com/1.1/statuses/update.json?status=hello' 
      --header 'authorization: OAuth
      oauth_consumer_key="oauth_customer_key",
      oauth_nonce="generated_oauth_nonce",
      oauth_signature="generated_oauth_signature",
      oauth_signature_method="HMAC-SHA1",
      oauth_timestamp="generated_timestamp",
      oauth_token="oauth_token",
      oauth_version="1.0"'
    """
    def createTweet(self, text):
        """
        Cria um tweet.
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update
        """
        requestUrl = self.base_url + '/1.1/statuses/update.json'
        response = requests.post(
            url=requestUrl,
            headers={'content-type': 'multipart/form-data'},
            data={
                'media': [],
                'status': text  # Texto do tweet
            }
        )
        fudeu = 1
