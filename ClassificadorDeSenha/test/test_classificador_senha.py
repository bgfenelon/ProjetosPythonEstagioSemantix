import unittest

from classificador_de_senha.classificar_senha_bianca import classificar_senha


class TestClassificarSenha(unittest.TestCase):


    def test_classificar_senha(self):
        #Cenario 1 entrada com senha vazia
        self.assertEqual(classificar_senha(''), 0)


        #Cenario 2 entrada tipo numerico
        self.assertFalse(classificar_senha(123))


        # Cenario 3 senha Média
        self.assertEqual(classificar_senha('minhasenha123'),1)


        #Cenario 4 senha Forte
        self.assertEqual(classificar_senha('minhaSenha123Bia'),2)



if __name__ == '__main__':
    unittest.main()