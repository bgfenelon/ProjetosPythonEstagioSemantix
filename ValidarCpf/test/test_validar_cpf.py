import unittest


from validar_cpf.validarcpf_bianca import valida_cpf
from validar_cpf.validarcpf_bianca import retira_formatacao


class TestValidarCpf(unittest.TestCase):


    def test_retirar_formatacao(self):
        #Cenario 1 tipo de fromatação
        self.assertTrue(retira_formatacao('387.467.498-93'))

        #Cenario 2 outro tipo de formatação
        self.assertTrue(retira_formatacao('387_467_498_93'))

        #Cenario 3 entrada Inesperada
        self.assertEqual(retira_formatacao(38746749893), 0)

        #Cenario 4 entrada Nula
        try:
            self.assertFalse(valida_cpf())
        except TypeError:
            print("Função não recebe Nulos! ")

    def test_validar_numero(self):

        # Cenario 1 tipo de fromatação
        self.assertTrue(valida_cpf(retira_formatacao('38746749893')))

        # Cenario 2 todos numeros repetidos
        self.assertTrue(valida_cpf(retira_formatacao('11111111111')))

        # Cenario 3 numeros a mais
        self.assertTrue(valida_cpf(retira_formatacao('3874674989334')))

        # Cenario 4 faltando numero
        self.assertTrue(valida_cpf(retira_formatacao('387467498')))

        # Cenario 5 recebendo 0
        self.assertEqual(valida_cpf(0), 0)

        # Cenario 6 entrada Nula

        try:
            self.assertFalse(valida_cpf())
        except TypeError:
            print("Função não recebe Nulos! ")





if __name__ == '__main__':
    unittest.main()