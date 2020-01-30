import unittest

from puctuation_cleaner import remova_puct


class TestRemovaPuct(unittest.TestCase):

    def test_tipo_de_arquivo_nao_existe(self):
        txt = "../arquivos/texto.json"
        remover = remova_puct(txt)
        self.assertEqual(remover, "Arquivo não existe")

    def test_entrana_inesperada(self):
        txt = 20
        remover = remova_puct(txt)
        self.assertEqual(remover, 0)

    def test_entrada_esperada(self):
        txt = "texto.txt"
        remover = remova_puct(txt)
        self.assertEqual(type(remover), str)

    def test_uma_string_qualquer(self):
        txt ="txtoQaulquer"
        remover = remova_puct(txt)
        self.assertEqual(remover, "Arquivo não existe")

    def test_retorna_texto_sem_pontuacao(self):
        txt = "../textoPontuacao.txt"
        remover = remova_puct(txt)
        self.assertEqual(remover, "palavras nao voce equaçao estaçoes saude sinonimo virgula ")



if __name__ == ' __main__ ':
    unittest.main()
