 #language: pt

Funcionalidade: Validar string

    Cenário: validar texto sem 'trigo', com opcao True
        Dado o texto: 'texto sem', e a opcao: True
        Quando eu verifico
        Então ele retorna False

    Cenário: validar texto com 'trigo', com opcao True
        Dado o texto: 'texto com trigo', e a opcao: True
        Quando eu verifico
        Então ele retorna True

    Cenário: validar texto vazio, com opcao True
        Dado o texto: '', e a opcao: True
        Quando eu verifico
        Então ele retorna False

    Cenário: validar texto vazio, com opcao False
        Dado o texto: '', e a opcao: False
        Quando eu verifico
        Então ele retorna False

    Cenário: validar texto sem 'Triticum', com opcao False
        Dado o texto: 'com a palavra', e a opcao: False
        Quando eu verifico
        Então ele retorna False

    Cenário: validar texto com 'Triticum', com opcao False
        Dado o texto: 'com a palavra Triticum', e a opcao: False
        Quando eu verifico
        Então ele retorna True