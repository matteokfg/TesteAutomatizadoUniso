from behave import given, when, then
from projeto import recebe_prompt

@given("o texto: '{texto}'")
def definir_texto(context, texto):
    context.texto = texto

@when('eu valido')
def validar_prompt(context):
    context.resultado_booleano, context.resultado_texto = recebe_prompt(context.texto)

@then("ele retorna {booleano} e '{texto_resultado}'")
def verificar_resultado(context, booleano, texto_resultado):
    assert (context.resultado_booleano, context.resultado_texto) == bool(booleano), texto_resultado