import unittest

from Projetos.CalcularFeriados.calcular_feriados import CalcularFeriado


class TestCalcularFeriados(unittest.TestCase):

    cf = CalcularFeriado()

    def test_entrada_de_uma_string_como_parametro(self):
        self.assertEqual(type(self.cf.contarFeriados("bianljnkhjca")),int)

    def test_verificandoa_a_data_da_pascoa_esta_certa(self):
        data2019 = self.cf.contarFeriados(2019)
        data2018 = self.cf.contarFeriados(2018)
        data2017 = self.cf.contarFeriados(2017)
        data2016 = self.cf.contarFeriados(2016)

        self.assertEqual(data2019["pascoa"], "21/4/2019")
        self.assertEqual(data2018["pascoa"], "1/4/2018")
        self.assertEqual(data2017["pascoa"], "16/4/2017")
        self.assertEqual(data2016["pascoa"], "27/3/2016")

    def test_passar_ano_antes_de_1850(self):
        self.assertEqual(self.cf.contarFeriados(1700),"Ano não existe")



def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalcularFeriados('test_entrada_de_uma_string_como_parametro'))
    suite.addTest(TestCalcularFeriados('test_verificandoa_a_data_da_pascoa_esta_certa'))
    suite.addTest(TestCalcularFeriados('test_passar_ano_antes_de_1850'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

