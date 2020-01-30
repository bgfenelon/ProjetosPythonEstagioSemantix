import unittest

from conta_palavras import conta_palavras


class TestContaPalavras(unittest.TestCase):

    def test_tipo_de_arquivo_nao_existe(self):
        txt = "Arquivotexto.txt"
        palavras = conta_palavras(txt)
        self.assertEqual(palavras, "Arquivo não existe")

    def test_entrada_caminho_não_existe(self):
        txt = "texto/texto.txt"
        palavras = conta_palavras(txt)
        self.assertEqual(palavras, "Arquivo não existe")

    def test_entrada_esperada(self):
        txt = "../texto.txt"
        palavras = conta_palavras(txt)
        self.assertEqual(palavras, [{'por': 2, 'você': 2, 'ficar': 1}])


    def test_texto_vazio(self):
        txt = "../textoVazio.txt"
        palavras = conta_palavras(txt)
        self.assertEqual(palavras, [{}])



if __name__ == ' __main__ ':
    unittest.main()