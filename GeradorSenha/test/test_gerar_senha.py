import unittest

from gerador_senha.gerar_senha_bianca import gerar_senha


class TestGeradoDeSenha(unittest.TestCase):


    def test_conta_zeros(self):

        #Cenario 1 testando se a senha tem 8 caracteres
        self.assertTrue(gerar_senha())

        #Cenario 2 tipo do valor retornado
        self.assertEqual(type(gerar_senha()),str)

        #Cenario 3 se contem numeros na senha
        self.assertTrue(gerar_senha())



if __name__ == '__main__':
    unittest.main()