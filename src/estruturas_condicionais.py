import math


def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


def raiz_quadrada_ou_numero_invalido(a):
    if a > 0:
        return math.sqrt(a)
    elif a < 0:
        return "Numero Invalido"
    else:
        return 0
