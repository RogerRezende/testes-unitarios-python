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

if __name__ == '__main__':
    unittest.main()
