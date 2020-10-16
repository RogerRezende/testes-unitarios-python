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

    def test_maior_numero3(self):
        # Arrange
        a = 30
        b = 30

        # Act
        resultado = maior_numero(a, b)

        # Assert
        self.assertEqual(resultado, "Numeros Iguais")

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

    def test_raiz_quadrada_ou_quadrado1(self):
        # Arrange
        a = 9

        # Act
        resultado = raiz_quadrada_ou_quadrado(a)

        # Assert
        self.assertEqual(resultado, 3)

    def test_raiz_quadrada_ou_quadrado2(self):
        # Arrange
        a = -9

        # Act
        resultado = raiz_quadrada_ou_quadrado(a)

        # Assert
        self.assertEqual(resultado, 81)

    def test_par_ou_impar1(self):
        # Arrange
        a = 7

        # Act
        resultado = par_ou_impar(a)

        # Assert
        self.assertEqual(resultado, "impar")

    def test_par_ou_impar2(self):
        # Arrange
        a = 32

        # Act
        resultado = par_ou_impar(a)

        # Assert
        self.assertEqual(resultado, "par")

    def test_maior_e_diferenca1(self):
        # Arrange
        a = 32
        b = 23

        # Act
        resultado = maior_e_diferenca(a, b)

        # Assert
        self.assertEqual(resultado, "maior - {} - diferenca - {}".format(a, a - b))

    def test_maior_e_diferenca2(self):
        # Arrange
        a = 22
        b = 44

        # Act
        resultado = maior_e_diferenca(a, b)

        # Assert
        self.assertEqual(resultado, "maior - {} - diferenca - {}".format(b, b - a))

    def test_media_aluno_ou_nota_invalida1(self):
        # Arrange
        a = 8
        b = 6

        # Act
        resultado = media_aluno_ou_nota_invalida(a, b)

        # Assert
        self.assertEqual(resultado, 7)

    def test_media_aluno_ou_nota_invalida2(self):
        # Arrange
        a = -1
        b = 7

        # Act
        resultado = media_aluno_ou_nota_invalida(a, b)

        # Assert
        self.assertEqual(resultado, "Nota Invalida")

    def test_media_aluno_ou_nota_invalida3(self):
        # Arrange
        a = 10
        b = 15

        # Act
        resultado = media_aluno_ou_nota_invalida(a, b)

        # Assert
        self.assertEqual(resultado, "Nota Invalida")

    def test_emprestimo1(self):
        # Arrange
        salario = 1000
        prestacao_emprestimo = 100

        # Act
        resultado = emprestimo(salario, prestacao_emprestimo)

        # Assert
        self.assertEqual(resultado, "Emprestimo concedido")

    def test_emprestimo2(self):
        # Arrange
        salario = 1000
        prestacao_emprestimo = 250

        # Act
        resultado = emprestimo(salario, prestacao_emprestimo)

        # Assert
        self.assertEqual(resultado, "Emprestimo nao concedido")

    def test_peso_ideal1(self):
        # Arrange
        altura = 1.80
        sexo = "homem"

        # Act
        resultado = peso_ideal(altura, sexo)

        # Assert
        self.assertEqual(resultado, 72.86)

    def test_peso_ideal2(self):
        # Arrange
        altura = 1.80
        sexo = "mulher"

        # Act
        resultado = peso_ideal(altura, sexo)

        # Assert
        self.assertEqual(resultado, 67.08)

if __name__ == '__main__':
    unittest.main()
