import google.generativeai as genai
from token_api import ClientGenAITokenClass as Token
import re

def valida_string(text, option=False):
    """Funcao que recebe string e confirma que contem a palavra 'trigo'(opcao True) ou 'Triticum'(opcao False)."""
    if option:
        regex = ".*(trigo|Trigo)+.*"
    else:
        regex = ".*(Triticum)+.*"

    if isinstance(text, str):
        if re.match(regex, text):
            return True
    return False

def recebe_prompt(texto):
    """Funcao que recebe texto, valida e retorna um booleano e um texto."""
    if valida_string(texto, True) and texto != "":
        return True, texto
    else:
        return False, "Prompt com erro"

def conecta_googlegenai():
    None

def retorna_resposta():
    None