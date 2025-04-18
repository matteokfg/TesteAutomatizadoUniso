import google.generativeai as genai
from token_api import ClientGenAITokenClass as Token
import re

def valida_string(text, option=False):
    """Funcao que recebe string e confirma que contem a palavra 'trigo'(opcao True) ou 'Triticum'(opcao False)."""
    if option:
        regex = ".*(trigo|Trigo)+.*"
    else:
        regex = ".*(Triticum)+.*"

    if re.match(regex, text):
        return True
    else:
        return False

def recebe_prompt():
    None

def conecta_googlegenai():
    None

def retorna_resposta():
    None