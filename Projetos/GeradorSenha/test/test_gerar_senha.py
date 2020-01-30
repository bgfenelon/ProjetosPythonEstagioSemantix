import unittest
from Projetos.GeradorSenha.gerar_senha_bianca import GerarSenha

class TestGeradoDeSenha(unittest.TestCase):

    gr = GerarSenha()

    def test_conta_zeros(self):

        #Cenario 1 testando se a senha tem 8 caracteres
        self.assertTrue(self.gr.gerar_senha())

        #Cenario 2 tipo do valor retornado
        self.assertEqual(type(self.gr.gerar_senha()),str)

        #Cenario 3 se contem numeros na senha
        self.assertTrue(self.gr.gerar_senha())

if __name__ == '__main__':
    unittest.main()