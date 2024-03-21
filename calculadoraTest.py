import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 2), 3)
        self.assertEqual(subtracao(-1, -1), 0)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(-1, 1), -1)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(0, 5), 0)

    def test_divisao_por_zero(self):
        self.assertEqual(divisao(6, 0), "Não é possivel dividir por zero")
        self.assertEqual(divisao(10, 0), "Não é possivel dividir por zero")

if __name__ == '__main__':
    unittest.main()