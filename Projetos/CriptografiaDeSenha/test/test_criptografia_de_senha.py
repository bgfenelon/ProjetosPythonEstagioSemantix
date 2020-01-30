import unittest

from criptografia_de_senha.criptografia_de_senha_bianca import hash_md5
from criptografia_de_senha.criptografia_de_senha_bianca import hash_sha256

class TestCriptografiaDeSenha(unittest.TestCase):


    def test_hash_md5(self):
        #Cenario 1 entrada esperada
        self.assertTrue( hash_md5('umasenhaqualquer'))

        #Cenario 2 comparando senhas
        senha1 = 'bianca'
        senha2 = 'bianca'
        saida1 = hash_md5(senha1)
        saida2 = hash_md5(senha2)
        self.assertEqual(saida1,saida2)

        #Cenario 3 entrada inesperado
        self.assertEqual(hash_md5(123456), 0 )

        #Cenario 4 entrada Nula
        try:
            self.assertFalse(hash_md5())
        except TypeError:
            print("Função não recebe Nulos! ")


    def test_hash_hash_sha256(self):
        #Cenario 1 entrada esperada
        self.assertTrue( hash_sha256('umasenhaqualquer'))

        #Cenario 2 comparando senhas
        senha1 = 'senhaa'
        senha2 = 'senhaa'
        saida1 = hash_sha256(senha1)
        saida2 = hash_sha256(senha2)
        self.assertEqual(saida1,saida2)

        #Cenario 3 entrada inesperado
        self.assertEqual(hash_sha256(123456), 0 )

        #Cenario 4 entrada Nula
        try:
            self.assertFalse(hash_sha256())
        except TypeError:
            print("Função não recebe Nulos! ")





if __name__ == '__main__':
    unittest.main()