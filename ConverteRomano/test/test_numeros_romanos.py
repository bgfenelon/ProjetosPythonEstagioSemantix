import unittest

from converte_romano.converte_romano_bianca import numero_para_romano
from converte_romano.converte_romano_bianca import valida_numero


class TestNumerosRomanos(unittest.TestCase):

    def test_validar_numer(self):

        #Cenario 1 entrada esperada
        self.assertTrue(valida_numero(5))

        #Cenario 2 entrada 0 ou maior que 3000
        self.assertFalse(valida_numero(4456))

        #Cenario 3 entrada Inesperada
        self.assertFalse(valida_numero("Olá"))
        #
        #Cenario 4 entrada com valor Decimal
        self.assertEqual(valida_numero(10.0), 0)

        #Cenario 5 entrada Nula
        try:
            self.assertFalse(valida_numero())
        except TypeError:
            print("Função não recebe Nulos! ")

    def test_converter_num_romano(self):

        #Cenario 1 entrada do valor esperada
        self.assertTrue(numero_para_romano(valida_numero(10)))

        #Cenario 2 entrada 0
        self.assertFalse(numero_para_romano(valida_numero(0)))


        # Cenário 3 retorno do valor esperado
        x = type(numero_para_romano(valida_numero(10)))
        self.assertEqual(x,str)

        # Cenário 4 retorno do valor NÃO esperado
        x = numero_para_romano(valida_numero(0))
        self.assertEqual(x,0)


if __name__ == '__main__':
    unittest.main()