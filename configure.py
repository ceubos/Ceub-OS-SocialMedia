import src.console as console
import src.configurations.for_twitter as twitter_config
import os
import sys

"""
Script de configuração.
"""
os.environ['DOT_ENV_PATH'] = os.getcwd() + '/.env'

console.printLine("Configurar")
if console.getInputAsBoolean('Deseja mesmo configurar? Qualquer configuração anterior será desfeita...') is True:
    try:
        if os.path.isfile(os.getenv('DOT_ENV_PATH')) is True:
            os.remove('.env')
        configurationFile = open(os.environ['DOT_ENV_PATH'], 'a')
        if console.getInputAsBoolean('Gostaria de configurar o Twitter?') is True:
            console.printLine('-- Twitter --')
            twitter_config.configureTwitter(configurationFile)

    except OSError:
        console.printErrorLine("Por favor dê permissão para criação de arquivos na pasta, dica: chmod -R 777 *.")
        sys.exit()
console.printLine("Configuração concluída")
