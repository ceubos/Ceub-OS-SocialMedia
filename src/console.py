import sys

"""
Pacote destinado para facilitação de interação com terminal.
"""
ansi_red = '\033[0;31m'
ansi_green = '\033[0;32'
ansi_terminator = '\033[0m'
line_break = '\n'


def printLine(message):
    """
    Envia para o console uma mensagem.
    """
    sys.stdout.write(message + line_break)


def printErrorLine(message):
    """
    Envia para o console uma linha de erro.
    :param message:
    :return:
    """
    sys.stdout.write(ansi_red + message + ansi_terminator + line_break)


def printSuccessLine(message):
    """
    Envia para o console uma linha de sucesso.
    :param message:
    :return:
    """
    sys.stdout.write(ansi_green + message + ansi_terminator + line_break)


def getInput(question):
    """
    Obtém um input.
    :param question:
    :return:
    """
    return input(question)


def getInputAsBoolean(question):
    """
    Obtém input como booleano.
    :param question: Pergunta para obter o input
    :return: True | False
    """
    printLine(question)
    printLine("-- digite yes(y) para sim ou no(n) para não")
    value = getInput('#?')
    if value == 'y' or value == 'yes':
        return True
    elif value == 'n' or value == 'no':
        return False
    return getInputAsBoolean(question)
