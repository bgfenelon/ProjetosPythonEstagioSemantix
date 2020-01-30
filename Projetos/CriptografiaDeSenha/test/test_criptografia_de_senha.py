import unittest

from Projetos.CriptografiaDeSenha.criptografia_de_senha_bianca import CriptografiaSenha

class TestCriptografiaDeSenha(unittest.TestCase):

    cs = CriptografiaSenha()

    def test_hash_md5(self):
        #Cenario 1 entrada esperada
        self.assertTrue( self.cs.hash_md5('umasenhaqualquer'))

        #Cenario 2 comparando senhas
        senha1 = 'bianca'
        senha2 = 'bianca'
        saida1 = self.cs.hash_md5(senha1)
        saida2 = self.cs.hash_md5(senha2)
        self.assertEqual(saida1,saida2)

        #Cenario 3 entrada inesperado
        self.assertEqual(self.cs.hash_md5(123456), 0 )

        #Cenario 4 entrada Nula
        self.assertEqual(self.cs.hash_md5(None),0)


    def test_hash_hash_sha256(self):
        #Cenario 1 entrada esperada
        self.assertTrue( self.cs.hash_sha256('umasenhaqualquer'))

        #Cenario 2 comparando senhas
        senha1 = 'senhaa'
        senha2 = 'senhaa'
        saida1 = self.cs.hash_sha256(senha1)
        saida2 = self.cs.hash_sha256(senha2)
        self.assertEqual(saida1,saida2)

        #Cenario 3 entrada inesperado
        self.assertEqual(self.cs.hash_sha256(123456), 0 )

        #Cenario 4 entrada Nula
        self.assertEqual(self.cs.hash_sha256(None),0)


if __name__ == '__main__':
    unittest.main()