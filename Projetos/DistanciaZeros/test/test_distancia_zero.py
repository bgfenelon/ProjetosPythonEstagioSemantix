import unittest

from distancia_zeros.conta_zeros_bianca import conta_zeros


class TestDistanciaZero(unittest.TestCase):


    def test_conta_zeros(self):
        #Cenario 1 entrada esperada
        self.assertTrue(conta_zeros('100, 2980, 367, 2000, representação'))

        #Cenario 2 entrada inesperada
        self.assertEqual(conta_zeros(0), 0)

        # Cenario 3 retorno esperado
        self.assertEqual(type(conta_zeros('100')),int)

        #Cenario 4 entrada Nula
        try:
            self.assertFalse(conta_zeros())
        except TypeError:
            print("Função não recebe Nulos! ")

        #cenario 5 testando outro valor
        self.assertTrue(conta_zeros('rdf0000wsdrt00000d0w0e0r000g00f0d00000'))


if __name__ == '__main__':
    unittest.main()