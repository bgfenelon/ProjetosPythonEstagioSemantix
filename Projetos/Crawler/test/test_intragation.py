import unittest
import requests

from services.tag_clear import remove_tags
from services.puctuation_cleaner import remova_puct
from services.remove_stopwords import remova_stopwords
from services.word_count import conta_palavras


class TestIntegration(unittest.TestCase):

    def test_integration_services(self):
        link = "https://gshow.globo.com/novelas/a-dona-do-pedaco/vem-por-ai/noticia/maria-da-paz-volta-a-fabrica-em-grande-estilo.ghtml"
        html = requests.get(link).text

        tag = remove_tags(html)
        puc = remova_puct(tag)
        stop = remova_stopwords(puc)
        conta = conta_palavras(stop)

        self.assertTrue(tag)
        self.assertTrue(puc)
        self.assertTrue(stop)
        self.assertEqual(conta, [('paz', 8), ('dona', 5), ('bolos', 5), ('pedaço', 4),
                                 ('vídeos', 3), ('maria', 3), ('fábrica', 3), ('vem', 2),
                                 ('aí', 2), ('capítulos', 2), ('fale', 2), ('conosco', 2),
                                 ('especiais', 2), ('novelas', 2), ('volta', 2), ('boleira', 2),
                                 ('reassume', 2), ('juliana', 2), ('paes', 2), ('voltei', 2), ('gshowcom', 1),
                                 ('página', 1), ('inicial', 1), ('resumo', 1), ('semana', 1), ('todos', 1),
                                 ('cardápio', 1), ('best', 1), ('cake', 1), ('receita', 1), ('carinho', 1),
                                 ('beleza', 1), ('cara', 1), ('feito', 1), ('moça', 1), ('chocolates', 1),
                                 ('garoto', 1), ('trilha', 1), ('sonora', 1), ('podcast', 1), ('personagens', 1),
                                 ('chamadas', 1), ('globoplay', 1), ('seis', 1), ('malhação', 1), ('toda', 1),
                                 ('forma', 1), ('amar', 1), ('bom', 1), ('sucesso', 1), ('grande', 1), ('estilo', 1),
                                 ('função', 1), ('derruba', 1), ('ordens', 1), ('tiranas', 1), ('fabiana', 1),
                                 ('acompanhe', 1), ('cenas', 1), ('próximos', 1), ('novela', 1), ('9', 1), ('18112019', 1),
                                 ('06h30', 1), ('atualizado', 1), ('20191118t093014963z', 1), ('surpreende', 1),
                                 ('funcionários', 1), ('foto', 1), ('tv', 1), ('globo', 1), ('finalmente', 1),
                                 ('realizou', 1), ('sonho', 1), ('ter', 1), ('após', 1), ('achar', 1), ('documento', 1),
                                 ('devolvia', 1), ('chega', 1), ('exultante', 1), ('local', 1), ('lado', 1),
                                 ('amadeu', 1), ('marcos', 1), ('palmeira', 1), ('>', 1), ('amigos', 1),
                                 ('pra', 1), ('maior', 1), ('alegria', 1), ('estar', 1), ('aqui', 1), ('sabem', 1),
                                 ('quanta', 1), ('saudade', 1), ('sentia', 1)])








