import unittest

from Projetos.ConverteRomano.converte_romano_bianca import ConverterNumeroParaRomano

class TestNumerosRomanos(unittest.TestCase):

    cr = ConverterNumeroParaRomano()

    def test_validar_numer(self):

        #Cenario 1 entrada esperada
        self.assertTrue(self.cr.valida_numero(5))

        #Cenario 2 entrada 0 ou maior que 3000
        self.assertFalse(self.cr.valida_numero(4456))

        #Cenario 3 entrada Inesperada
        self.assertFalse(self.cr.valida_numero("Olá"))
        #
        #Cenario 4 entrada com valor Decimal
        self.assertEqual(self.cr.valida_numero(10.0), 0)

        #Cenario 5 entrada Nula
        try:
            self.assertFalse(self.cr.valida_numero())
        except TypeError:
            print("Função não recebe Nulos! ")

    def test_converter_num_romano(self):

        #Cenario 1 entrada do valor esperada
        self.assertTrue(self.cr.numero_para_romano(10))

        #Cenario 2 entrada 0
        self.assertFalse(self.cr.numero_para_romano(0))


        # Cenário 3 retorno do valor esperado
        x = type(self.cr.numero_para_romano(10))
        self.assertEqual(x,str)

        # Cenário 4 retorno do valor NÃO esperado
        x = self.cr.numero_para_romano(0)
        self.assertEqual(x,0)


if __name__ == '__main__':
    unittest.main()