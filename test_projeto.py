import pytest
from projeto import recebe_prompt, conecta_googlegenai, retorna_resposta, valida_string

def test_valida_string():
    assert valida_string("Faça um breve texto sobre o trigo: Tricium aestivum L", '1') == True
    assert valida_string("Triticum aestivum L.", '2') == True
    assert valida_string("aestivum L.", '2') == False
    assert valida_string(7, '1') == False
    assert valida_string(7, '2') == False

def test_recebe_prompt():
    assert recebe_prompt("Sou um prompt") == (True, "Sou um prompt")
    assert recebe_prompt("") == (False, "Prompt com erro")
    assert recebe_prompt(7) == (False, "Prompt com erro")
    assert recebe_prompt(True) == (False, "Prompt com erro")
    assert recebe_prompt([]) == (False, "Prompt com erro")
    assert recebe_prompt({}) == (False, "Prompt com erro") 

def test_conecta_googlegenai():
    assert conecta_googlegenai("Faça um breve texto sobre a espécie de trigo: Tricium aestivum L")['returnCode'] == 200

def test_retorna_resposta():
    assert retorna_resposta(200, 
                            "O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
                        ) == "O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
    assert retorna_resposta(200, 
                            "O trigo, cientificamente conhecido como aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
                        ) == "Erro na resposta"
    assert retorna_resposta(400, "") == "Erro na resposta"
    assert retorna_resposta(False, "Prompt com erro") == "Prompt com erro"