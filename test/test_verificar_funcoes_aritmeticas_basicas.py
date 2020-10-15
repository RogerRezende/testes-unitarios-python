import unittest


class FuncoesAritmeticasBasicasTest(unittest.TestCase):
    def test_soma_correta(self):
        # Arrange
        a = 2
        b = 2

        # Act
        resultado = soma(a, b)

        # Assert
        self.assertEqual(resultado, 4)

    def test_subtracao_correta(self):
        # Arrange
        a = 2
        b = 2

        # Act
        resultado = subtracao(a, b)

        # Assert
        self.assertEqual(resultado, 0)
        
    def test_multiplicacao_correta(self):
        # Arrange
        a = 2
        b = 2

        # Act
        resultado = multiplicacao(a, b)

        # Assert
        self.assertEqual(resultado, 4)
        
    def test_divisao_correta(self):
        # Arrange
        a = 2
        b = 2

        # Act
        resultado = divisao(a, b)

        # Assert
        self.assertEqual(resultado, 1)
        
    def test_resto_correta(self):
        # Arrange
        a = 2
        b = 2

        # Act
        resultado = resto(a, b)

        # Assert
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
