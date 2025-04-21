from behave import given, when, then
from projeto import retorna_resposta


@given("o texto: {texto} e o codigo HTTPS {codigo}")
def definir_valor(context, texto, codigo):
    context.texto = texto
    context.codigo = int(codigo)

@when("eu recebo e verifico")
def verficar(context):
    context.resultado = retorna_resposta(context.codigo, context.texto)


@then("ele retorna o texto {resposta}")
def verificar_resultado(context, resposta):
    assert context.resultado == resposta