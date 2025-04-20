from behave import given, when, then
from projeto import recebe_prompt

@given("o prompt: {prompt}")
def definir_texto(context, prompt):
    context.prompt = prompt

@when('eu valido')
def validar_prompt(context):
    context.resultado_booleano, context.resultado_texto = recebe_prompt(context.prompt)

@then("ele retorna {booleano} e {texto_resultado}")
def verificar_resultado(context, booleano, texto_resultado):
    assert (context.resultado_booleano, context.resultado_texto) == (eval(booleano), texto_resultado)