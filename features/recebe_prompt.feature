#language: pt

Funcionalidade: Receber prompt

    Esquema do Cenário: recebe texto
        Dado o prompt: <prompt>
        Quando eu valido
        Então ele retorna <booleano> e <resposta>
        Exemplos:
            | prompt                                                    | booleano  | resposta                                              |
            | Faça um breve texto sobre o trigo: Tricium aestivum L     | True      | Faça um breve texto sobre o trigo: Tricium aestivum L |
            | ''                                                        | False     | Prompt com erro                                       |
