import pytest
from projeto import recebe_prompt, conecta_googlegenai, retorna_resposta, valida_string

def test_valida_string():
    assert valida_string("Faça um breve texto sobre o trigo: Tricium aestivum L", True) == True
    assert valida_string("Triticum aestivum L.") == True
    assert valida_string("aestivum L.") == False
    assert valida_string(7, True) == False
    assert valida_string(7, True) == False

def test_recebe_prompt():
    assert recebe_prompt("Faça um breve texto sobre o trigo: Tricium aestivum L") == (True, "Faça um breve texto sobre o trigo: Tricium aestivum L")
    assert recebe_prompt("") == (False, "Prompt com erro")
    assert recebe_prompt(7) == (False, "Prompt com erro")
    assert recebe_prompt(True) == (False, "Prompt com erro")
    assert recebe_prompt([]) == (False, "Prompt com erro")
    assert recebe_prompt({}) == (False, "Prompt com erro") 

def test_conecta_googlegenai():
    assert conecta_googlegenai("Faça um breve texto sobre a espécie de trigo: Tricium aestivum L")['return_Https_Code'] == 200

def test_retorna_resposta():
    assert retorna_resposta(200, 
                            "O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
                        ) == "O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
    assert retorna_resposta(200, 
                            "O trigo, cientificamente conhecido como aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras."
                        ) == "Erro na resposta"
    assert retorna_resposta(400, "") == "Erro na resposta"
    assert retorna_resposta(False, "Prompt com erro") == "Prompt com erro"