import pytest
from projeto import recebe_prompt, conecta_googlegenai, retorna_resposta

#preencher "" com prompt de exemplo/teste

def test_recebe_prompt():
    assert recebe_prompt("Sou um prompt") == (True, "Sou um prompt")
    assert recebe_prompt("") == (False, "Prompt com erro")
    assert recebe_prompt(7) == (False, "Prompt com erro")
    assert recebe_prompt(True) == (False, "Prompt com erro")
    assert recebe_prompt([]) == (False, "Prompt com erro")
    assert recebe_prompt({}) == (False, "Prompt com erro") 

def test_conecta_googlegenai():
    assert conecta_googlegenai("") == {'returnCode': 200, 'returnData': ""}
    assert conecta_googlegenai("") == {'returnCode': 400}

def test_retorna_resposta():
    assert retorna_resposta(200, "") == ""
    assert retorna_resposta(200, "") == "Erro na resposta" #resposta não contem palavra chave
    assert retorna_resposta(400, "") == "Erro na resposta"
    assert retorna_resposta(False, "Prompt com erro") == "Prompt com erro"