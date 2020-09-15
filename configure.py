import src.console
import os
from dotenv import load_dotenv

load_dotenv()

print("Configurar credênciais:")
src.console.printLine("Configurando para: Facebook")
wantsToConfigureFacebook = \
    src.console.getInputAsBoolean(question="Gostaria de configurar para o facebook")

if wantsToConfigureFacebook is True:
    fbClientId = None
    fbClientSecret = None
    while fbClientSecret is None or fbClientSecret is None:
        fbClientId = src.console.getInput(question="facebook client id>:")
        fbClientSecret = src.console.getInput(question="facebook client secret>:")
