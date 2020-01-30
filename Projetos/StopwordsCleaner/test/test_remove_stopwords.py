import unittest

from Projetos.StopwordsCleaner.remove_stopwords import RemovaStopWords

class TestRemovaStopWords(unittest.TestCase):
    rs = RemovaStopWords()

    def test_tipo_de_arquivo_nao_existe(self):
        txt = "../arquivos/texto.json"
        remover = self.rs.remova_stopwords(txt)
        self.assertEqual(remover, "Arquivo não existe")

    def test_entrana_inesperada(self):
        txt = 356
        remover = self.rs.remova_stopwords(txt)
        self.assertEqual(remover, 0)

    def test_entrada_esperada(self):
        txt = "texto.txt"
        remover = self.rs.remova_stopwords(txt)
        self.assertEqual(type(remover), str)

    def test_retorna_o_texto_realmente_sem_stop_word(self):
        txt = "texto.txt"
        remover = self.rs.remova_stopwords(txt)
        lista = remover.split()
        for x in lista:
            if x == 'a':
                result = 'existe'
            elif x != 'a':
                result = 'nao existe storwords'

        self.assertEqual(result, 'nao existe storwords')


if __name__ == '__main__':
    unittest.main()
