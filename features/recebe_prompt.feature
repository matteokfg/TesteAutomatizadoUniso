#language: pt

Funcionalidade: Receber prompt

    Esquema do Cenário: recebe texto
        Dado o prompt: <prompt>
        Quando eu valido
        Então ele retorna True e <resposta>
        Exemplos:
            | prompt                                                    | resposta                                              |
            | Faça um breve texto sobre o trigo: Tricium aestivum L     | Faça um breve texto sobre o trigo: Tricium aestivum L |
            |                                                           | Prompt com erro                                       |
