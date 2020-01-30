import unittest

from Projetos.WordCount.conta_palavras import ContarPalavra


class TestContaPalavras(unittest.TestCase):
    cp = ContarPalavra()

    def test_tipo_de_arquivo_nao_existe(self):
        txt = "Arquivotexto.txt"
        palavras = self.cp.conta_palavras(txt)
        self.assertEqual(palavras, "Arquivo não existe")

    def test_entrada_caminho_não_existe(self):
        txt = "texto/texto.txt"
        palavras = self.cp.conta_palavras(txt)
        self.assertEqual(palavras, "Arquivo não existe")

    def test_entrada_esperada(self):
        txt = "../texto.txt"
        palavras = self.cp.conta_palavras(txt)
        self.assertEqual(palavras, [{'por': 2, 'você': 2, 'ficar': 1}])

    def test_texto_vazio(self):
        txt = "../textoVazio.txt"
        palavras = self.cp.conta_palavras(txt)
        self.assertEqual(palavras, [])


if __name__ == ' __main__ ':
    unittest.main()
