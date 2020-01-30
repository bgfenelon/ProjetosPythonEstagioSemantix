import unittest

from Projetos.ValidarCpf.validarcpf_bianca import ValidarCPF

class TestValidarCpf(unittest.TestCase):

    vc = ValidarCPF()

    def test_retirar_formatacao(self):
        #Cenario 1 tipo de fromatação
        self.assertTrue(self.vc.retira_formatacao('387.467.498-93'))

        #Cenario 2 outro tipo de formatação
        self.assertTrue(self.vc.retira_formatacao('387_467_498_93'))

        #Cenario 3 entrada Inesperada
        self.assertEqual(self.vc.retira_formatacao(38746749893), 0)

        #Cenario 4 entrada Nula
        self.assertEqual(self.vc.valida_cpf(None),0)


    def test_validar_numero(self):

        # Cenario 1 tipo de fromatação
        self.assertTrue(self.vc.valida_cpf('38746749893'))

        # Cenario 2 todos numeros repetidos
        self.assertTrue(self.vc.valida_cpf('11111111111'))

        # Cenario 3 numeros a mais
        self.assertTrue(self.vc.valida_cpf('3874674989334'))

        # Cenario 4 faltando numero
        self.assertTrue(self.vc.valida_cpf('387467498'))

        # Cenario 5 recebendo 0
        self.assertEqual(self.vc.valida_cpf(0), 0)

        # Cenario 6 entrada Nula
        self.assertEqual(self.vc.valida_cpf(None),0)






if __name__ == '__main__':
    unittest.main()