import sys
sys.path.insert(0, '../src')
import unittest
from areas_figuras_planas import *


class AreasFigurasPlanasTests(unittest.TestCase):
    def test_area_quadrado_correta(self):
        # Arrange
        lado = 2

        # Act
        resultado = area_quadrado(lado)

        # Assert
        self.assertEqual(resultado, 4)

    def test_area_retangulo_correta(self):
        # Arrange
        base = 2
        altura = 3

        # Act
        resultado = area_retangulo(base, altura)

        # Assert
        self.assertEqual(resultado, 6)

    def test_area_paralelogramo_correta(self):
        # Arrange
        base = 3
        altura = 3

        # Act
        resultado = area_paralelogramo(base, altura)

        # Assert
        self.assertEqual(resultado, 9)

    def test_area_losango_correta(self):
        # Arrange
        diagonal_menor = 2
        diagonal_maior = 3

        # Act
        resultado = area_losango(diagonal_menor, diagonal_maior)

        # Assert
        self.assertEqual(resultado, 3)

    def test_area_trapezio_correta(self):
        # Arrange
        base_menor = 2
        base_maior = 3
        altura = 4

        # Act
        resultado = area_trapezio(base_menor, base_maior, altura)

        # Assert
        self.assertEqual(resultado, 10)

    def test_area_triangulo_qualquer_correta(self):
        # Arrange
        base = 3
        altura = 3

        # Act
        resultado = area_triangulo_qualquer(base, altura)

        # Assert
        self.assertEqual(resultado, 4.5)

    def test_area_triangulo_retangulo_correta(self):
        # Arrange
        base = 4
        altura = 4

        # Act
        resultado = area_triangulo_retangulo(base, altura)

        # Assert
        self.assertEqual(resultado, 8)

    def test_area_triangulo_equilatero_correta(self):
        # Arrange
        lado = 12

        # Act
        resultado = area_triangulo_equilatero(lado)

        # Assert
        self.assertEqual(resultado, 62.35) 

    def test_area_triangulo_formula_heron_correta(self):
        # Arrange
        lado_a = 26
        lado_b = 26
        lado_c = 20

        # Act
        resultado = area_triangulo_formula_heron(lado_a, lado_b, lado_c)

        # Assert
        self.assertEqual(resultado, 240)

    def test_area_circulo_correta(self):
        # Arrange
        raio = 2

        # Act
        resultado = area_circulo(raio)

        # Assert
        self.assertEqual(resultado, 12.57)

if __name__ == '__main__':
    unittest.main()
