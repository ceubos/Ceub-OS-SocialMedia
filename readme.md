### Automatizações para Marketing do Ceub OS

Repositório oficial: https://github.com/aderbalbotelho/CEUB-OS

Ainda não está funcionando!

#### Integrações:

Twitter 
> Referência: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update

Facebook
> Referência: https://developers.facebook.com/docs/pages/publishing

Instagram: 

#### Atividades 
- Criar integração com facebook 
- Criar integração com o twitter
- Criar integração com o instagram

#### Instruções
Download:
```bash 
git clone https://github.com/nickeatingsalsage/Ceub-OS-SocialMedia
```
Agora dentro da pasta execute os seguintes comandos: 
```bash
 touch .env
 echo "FACEBOOK_CLIENT_ID=[FACEBOOK CLIENT ID]
FACEBOOK_CLIENT_SECRET=[FACEBOOK CLIENT SECRET]
FACEBOOK_PAGE_ID=[FACEBOOK PAGE ID]" >> .env
```

#### Documentação

Váriaveis de ambiente(.env)
###### Facebook
  FACEBOOK_CLIENT_SECRET: credencial para obter access_token.
  
  FACEBOOK_CLIENT_ID: credencial para obter access_token, identifica o usuário.
  
  FACEBOOK_PAGE_ID:  Id da página do facebook no qual todas as publicações serão direcionadas.
#### Notas
Seria interessante criar no configure.py uma interface para inserir os tokens necessários automaticamente.


 
