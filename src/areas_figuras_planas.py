import math


def area_quadrado(lado):
    return lado * lado


def area_retangulo(base, altura):
    return base * altura


def area_paralelogramo(base, altura):
    return base * altura


def area_losango(diagonal_menor, diagonal_maior):
    return (diagonal_maior * diagonal_menor) / 2


def area_trapezio(base_menor, base_maior, altura):
    return ((base_maior * base_menor) * altura) / 2


def area_triangulo_qualquer(base, altura):
    return (base * altura) / 2


def area_triangulo_retangulo(base, altura):
    return (base * altura) / 2


def area_triangulo_equilatero(lado):
    return round(((lado * lado) * math.sqrt(3)) / 4, 2)


def area_triangulo_formula_heron(lado_a, lado_b, lado_c):
    p = (lado_a + lado_b + lado_c) / 2
    return round(math.sqrt(p * (p - lado_a) * (p - lado_b) * (p - lado_c)), 2)


def area_circulo(raio):
    return round(math.pi * raio * raio, 2)
