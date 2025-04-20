from behave import given, when, then
from projeto import recebe_prompt

@given("o prompt: {prompt}")
def definir_texto(context, prompt):
    context.prompt = prompt

@when('eu valido')
def validar_prompt(context):
    (resultado_booleano, resultado_texto) = recebe_prompt(context.prompt)
    context.resultado_booleano = resultado_booleano
    context.resultado_texto = resultado_texto

@then("ele retorna {booleano} e {texto_resultado}")
def verificar_resultado(context, booleano, texto_resultado):
    assert (context.resultado_booleano, context.resultado_texto) == (eval(booleano), texto_resultado)