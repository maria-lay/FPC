"""Atividade da calculadora de financiamento"""
lista_entrada = input().split()
operacao = int
x1 = int
x2 = int

# definindo variaveis a partir da leitura da entrada
if len(lista_entrada) == 2:
    operacao, x1_str = lista_entrada
    x1 = int(x1_str)
if len(lista_entrada) == 3:
    operacao, x1_str, x2_str = lista_entrada
    x1 = int(x1_str)
    x2 = int(x2_str)


def sucessor(x):
    x += 1
    return x


def somar(x, y):
    for i in range(y):
        x = sucessor(x)
    return x


def multiplicar(x, y):
    mult = 0
    for i in range(y):
        mult = somar(mult, x)
    return mult


def expo(x, y):
    exp = x
    for i in range(y - 1):
        exp = multiplicar(exp, x)
    return exp


if operacao.upper() == "SUC":
    print(sucessor(x1))
elif operacao.upper() == "SOMA":
    print(somar(x1, x2))
elif operacao.upper() == "MULT" or operacao.upper() == "MULTI":
    print(multiplicar(x1, x2))
elif operacao.upper() == "EXP":
    print(expo(x1, x2))
