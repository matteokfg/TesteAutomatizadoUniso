#language: pt

Funcionalidade: Retornar resposta da GenAI

    Cenário: recebe resposta correta
        Dado o texto: O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras. e o codigo HTTPS 200
        Quando eu recebo e verifico
        Então eu retorno o texto O trigo, cientificamente conhecido como Triticum aestivum L., é um cereal amplamente cultivado em todo o mundo, sendo uma das principais fontes de alimento para a humanidade. Pertencente à família das gramíneas (Poaceae), o trigo é caracterizado por suas espigas que contêm grãos ricos em carboidratos, proteínas e fibras.

    Cenário: recebe codigo errado
        Dado o texto: '' e o codigo HTTPS 400 
        Quando eu recebo e verifico
        Então eu retorno o texto Erro na resposta