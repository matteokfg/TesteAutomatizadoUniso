#language: pt

Funcionalidade: Receber prompt

    Esquema do Cenário: recebe texto
        Dado o texto: <texto>
        Quando eu valido
        Então ele retorna True e <resposta>
        Exemplos:
            | texto                                                     | resposta                                              |
            | Faça um breve texto sobre o trigo: Tricium aestivum L     | Faça um breve texto sobre o trigo: Tricium aestivum L |
            |                                                           | Prompt com erro                                       |
