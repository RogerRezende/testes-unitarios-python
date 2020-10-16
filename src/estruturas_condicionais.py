import math


def maior_numero(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Numeros Iguais"


def raiz_quadrada_ou_numero_invalido(a):
    if a > 0:
        return math.sqrt(a)
    elif a < 0:
        return "Numero Invalido"
    else:
        return 0


def raiz_quadrada_ou_quadrado(a):
    if a > 0:
        return math.sqrt(a)
    elif a < 0:
        return a * a
    else:
        return 0


def par_ou_impar(a):
    if a % 2 == 0:
        return "par"
    else:
        return "impar"


def maior_e_diferenca(a, b):
    if a > b:
        resultado = a - b
        return "maior - {} - diferenca - {}".format(a, resultado)
    else:
        resultado = b - a
        return "maior - {} - diferenca - {}".format(b, resultado)


def media_aluno_ou_nota_invalida(a, b):
    if a < 0 or a > 10:
        return "Nota Invalida"
    elif b < 0 or b > 10:
        return "Nota Invalida"
    else:
        return round((a + b) / 2, 1)


def emprestimo(salario, prestacao_emprestimo):
    if prestacao_emprestimo > salario * 0.2:
        return "Emprestimo nao concedido"
    else:
        return "Emprestimo concedido"


def peso_ideal(altura, sexo):
    if sexo == "homem":
        return round((72.7 * altura) - 58, 2)
    else:
        return round((62.1 * altura) - 44.7, 2)
