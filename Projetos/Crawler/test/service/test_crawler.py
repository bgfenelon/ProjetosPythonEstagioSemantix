import unittest

from services.crawler import crawler

class TestTagRemove(unittest.TestCase):
    def test_link_vazio(self):
        htmlVazio = crawler("")
        self.assertEqual(htmlVazio,"Link Vazio")

    def test_passando_link_nao_existe(self):
        caminhoErrado = crawler("https://github.com/bgfenelon/TagCleane/blob/masterhjshdkjhsak")
        self.assertEqual(caminhoErrado,"Link Não Existe")

    def test_passar_uma_pagina_sem_imagem(self):
        html = crawler('http://dontpad.com/askdad')
        self.assertTrue(html)

    def test_nao_passar_link_como_parametro(self):
        html = crawler(123)
        self.assertEqual(html, "Link Não Existe")

    def test_entrada_esperada(self):
        html = crawler("https://gshow.globo.com/novelas/a-dona-do-pedaco/vem-por-ai/noticia/maria-da-paz-volta-a-fabrica-em-grande-estilo.ghtml")
        self.assertTrue(html)

if __name__ == '__main__':
    unittest.main()