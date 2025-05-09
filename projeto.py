# import google.generativeai as genai
from google import genai
# from google.genai import types
from token_api import ClientGenAITokenClass
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
        return (True, texto)
    else:
        return (False, "Prompt com erro")

def conecta_googlegenai(prompt):
    TOKEN = ClientGenAITokenClass()
    # Only run this block for Gemini Developer API
    client = genai.Client(api_key=TOKEN.token)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    return response

def retorna_resposta(return_code, texto):
    if isinstance(texto, str) and texto != "":
        if return_code == 200 and valida_string(texto):
            return texto
    return "Erro na resposta"


if __name__ == "__main__":
    texto = input("Pergunte algo sobre trigo:\n   - ")
    booleano, texto = recebe_prompt(texto)
    if booleano:
        resposta = conecta_googlegenai(texto)
        texto_resposta = retorna_resposta(resposta['returnCode'], resposta.text)
        print(texto_resposta)
    else:
        print(texto)
