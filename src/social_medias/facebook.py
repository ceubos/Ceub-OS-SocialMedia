import os
import requests


class facebook:
    def getAccessToken(self):
        if os.getenv('FACEBOOK_ACCESS_TOKEN') is not None:
            return os.getenv('FACEBOOK_ACCESS_TOKEN')
        else:
            fbClientId = os.getenv('FACEBOOK_CLIENT_ID')
            fbClientSecret = os.getenv('FACEBOOK_CLIENT_SECRET')
            if fbClientId is not None and fbClientSecret is not None:
                response = requests.get(
                    'https://graph.facebook.com/oauth/access_token',
                    {
                        'grant_type': 'fb_exchange_token',
                        'client_id': fbClientId,
                        'client_secret': fbClientSecret,
                    }
                )


            raise Exception(
                "FACEBOOK_APP_ID, FACEBOOK_CLIENT_ID ou FACEBOOK_CLIENT_SECRET naõ configurados verifique o arquivo .env ou execute "
                "novamente: configure.py.")
