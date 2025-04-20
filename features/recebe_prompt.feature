#language: pt

Funcionalidade: Receber prompt

    Cenário: recebe texto
        Dado o texto: 'Faça um breve texto sobre o trigo: Tricium aestivum L'
        Quando eu valido
        Então ele retorna True e 'Faça um breve texto sobre o trigo: Tricium aestivum L'

    Cenário: recebe texto vazio
        Dado o texto: ''
        Quando eu valido
        Então ele retorna False e 'Prompt com erro'