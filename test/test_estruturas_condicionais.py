import sys
sys.path.insert(0, '../src')
import unittest
from estruturas_condicionais import *


class EstruturasCondicionaisTests(unittest.TestCase):
    def test_maior_numero1(self):
        # Arrange
        a = 2
        b = 1

        # Act
        resultado = maior_numero(a, b)

        # Assert
        self.assertEqual(resultado, a)

    def test_maior_numero2(self):
        # Arrange
        a = 5
        b = 10

        # Act
        resultado = maior_numero(a, b)

        # Assert
        self.assertEqual(resultado, b)

    def test_raiz_quadrada_ou_numero_invalido1(self):
        # Arrange
        a = 9

        # Act
        resultado = raiz_quadrada_ou_numero_invalido(a)

        # Assert
        self.assertEqual(resultado, 3)

    def test_raiz_quadrada_ou_numero_invalido2(self):
        # Arrange
        a = -9

        # Act
        resultado = raiz_quadrada_ou_numero_invalido(a)

        # Assert
        self.assertEqual(resultado, "Numero Invalido")

if __name__ == '__main__':
    unittest.main()
