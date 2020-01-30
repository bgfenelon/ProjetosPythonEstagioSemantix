import unittest

from Projetos.ValorMoedas.valor_moedas_bianca import ValorMoedas

class TestNumerosRomanos(unittest.TestCase):

    vm = ValorMoedas()

    def test_valor_moeda(self):

        #Cenario 1 entrada do valor esperada
        self.assertTrue(self.vm.valor_moeda(30.34))

        # Cenario 2 entrada 0
        self.assertEqual(self.vm.valor_moeda(0), 0)

        # Cenário 3 entrada com tipo de valor inesperado
        self.assertEqual(self.vm.valor_moeda("teste"),0)

        # Cenário 4 retorno do valor esperado
        self.assertEqual(type(self.vm.valor_moeda(20.34)),dict)


if __name__ == '__main__':
    unittest.main()