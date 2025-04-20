from behave import given, when, then
from projeto import valida_string

@given("o texto: {texto}, e a opcao: {opcao}")
def definir_valores(context, texto, opcao):
    context.texto = texto
    context.opcao = bool(opcao)

@when('eu verifico')
def validar_texto(context):
    context.resultado = valida_string(context.texto, context.opcao)

@then('ele retorna {resultado_esperado}')
def verificar_resultado(context, resultado_esperado):
    assert context.resultado == bool(resultado_esperado)