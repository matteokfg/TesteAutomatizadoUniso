#language: pt

Funcionalidade: Receber prompt

    Cenário: recebe texto
        Dado o texto: 'algum texto de prompt'
        Quando eu recebo e verifico
        Então ele retorna True e 'algum texto de prompt'

    Cenário: recebe texto vazio
        Dado o texto: ''
        Quando eu recebo e verifico
        Então ele retorna False e 'Prompt com erro'