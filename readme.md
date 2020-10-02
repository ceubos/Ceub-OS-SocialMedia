### Automatizações para Marketing do Ceub OS

Repositório oficial: https://github.com/aderbalbotelho/CEUB-OS


#### Integrações:

Twitter 
> Referência: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update

Facebook
> Referência: https://developers.facebook.com/docs/pages/publishing

Instagram: 

#### Atividades 
- Criar integração com facebook[?] 
- Criar integração com o twitter[OK]
- Criar integração com o instagram[?]

#### Instruções
Download:
```bash 
git clone https://github.com/ceubos/Ceub-OS-SocialMedia
```
**Instalando dependências:**

É necessário ter o "pip" em mãos.  
O pip é o gerenciador de pacotes padrão para o Python.  
Mais detalhes de como funciona acessando: https://packaging.python.org/tutorials/installing-packages/

```bash 
pip freeze > requirements.txt
```

#### Documentação

  
**Twitter**  
![alt text](https://help.twitter.com/content/dam/help-twitter/twitter_logo_blue.png "Logo Title Text 1")  
***Configurando ambiente***

Dentro do projeto execute o seguinte comando e siga as instruções:
```bash 
python configure.py
```   
ou configure um arquivo .env dentro do diretório com as seguintes váriaveis:
```bash
TWITTER_API_KEY=  
TWITTER_API_SECRET_KEY=  
TWITTER_API_ACCESS_TOKEN=  
TWITTER_API_ACCESS_TOKEN_SECRET=
```   
  

***Interagindo com o Twitter***

Para criar um tweet:

```bash 
python create_tweet.py 'Olá este é um tweet!'
```  

Observação:

O Twitter impede tweets repetidos em um espaço de tempo curto. Evite mandar strings de tweet repetidas.

#### Notas
Nada por enquanto...


 
