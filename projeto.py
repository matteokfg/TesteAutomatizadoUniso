# import google.generativeai as genai
from google import genai
from google.genai import types
from pydantic import BaseModel
from token_api import ClientGenAITokenClass
import re

class Resposta(BaseModel):
    return_Https_Code = int
    texto: str

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
        model='gemini-2.0-flash-001', contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'respose_schema': Resposta
        }
    )
    print(response.text)
    return response.text

def retorna_resposta(return_code, texto):
    if isinstance(texto, str) and return_code == 200:
        if valida_string(texto) and texto != "":
            return texto
    return "Prompt com erro"


if __name__ == "__main__":
    texto = input()
    booleano, texto = recebe_prompt(texto)
    if booleano:
        resposta = conecta_googlegenai(texto)
        texto_resposta = retorna_resposta(resposta['return_Https_Code'], resposta['texto'])
        print(texto_resposta)
    else:
        print(texto)
