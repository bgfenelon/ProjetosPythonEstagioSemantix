import unittest

from valor_moedas_bianca import valor_moeda


class TestNumerosRomanos(unittest.TestCase):


    def test_valor_moeda(self):

        #Cenario 1 entrada do valor esperada
        self.assertTrue(valor_moeda(30.34))

        # Cenario 2 entrada 0
        self.assertEqual(valor_moeda(0), 0)

        # Cenário 3 entrada com tipo de valor inesperado
        self.assertEqual(valor_moeda("teste"),0)

        # Cenário 4 retorno do valor esperado
        self.assertEqual(type(valor_moeda(20.34)),dict)


if __name__ == '__main__':
    unittest.main()