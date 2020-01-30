import unittest

from Projetos.ClassificadorDeSenha.classificar_senha_bianca import ClassificarSenha


class TestClassificarSenha(unittest.TestCase):

    cs = ClassificarSenha()

    def test_classificar_senha(self):
        #Cenario 1 entrada com senha vazia
        self.assertEqual(self.cs.classificar_senha(''), 0)
        #Cenario 2 entrada tipo numerico
        self.assertFalse(self.cs.classificar_senha(123))
        # Cenario 3 senha Média
        self.assertEqual(self.cs.classificar_senha('minhasenha123'),1)
        #Cenario 4 senha Forte
        self.assertEqual(self.cs.classificar_senha('minhaSenha123Bia'),2)

if __name__ == '__main__':
    unittest.main()