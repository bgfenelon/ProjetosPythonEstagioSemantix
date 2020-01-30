import unittest

from Projetos.TagCleane.tag_cleaner import RemoverTags

class TestTagRemove(unittest.TestCase):

    rt = RemoverTags()

    def test_texto_do_html_vazio(self):
        # passando html sem texto
        htmlVazio = self.rt.remove_tags("../htmls/htmlVazio.txt")
        self.assertEqual(htmlVazio,"Texto Vazio")

    def test_passando_caminho_errado(self):
        #passando com caminho errado / não existe
        caminhoErrado = self.rt.remove_tags("html.txt")
        self.assertEqual(caminhoErrado,"Caminho errado !")

    def test_entrada_esperada(self):
        html = self.rt.remove_tags("../htmls/html.txt")
        self.assertTrue(html)

    def test_html_com_alguma_tag_quebrada(self):
        html = self.rt.remove_tags("../htmls/htmlQuebrado.txt")
        self.assertTrue(html)

    def test_arquivo_nao_e_txt(self):
        html = self.rt.remove_tags("../htmls/html.json")
        self.assertTrue(html)

if __name__ == '__main__':
    unittest.main()
