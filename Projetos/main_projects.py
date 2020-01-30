from Projetos.CalcularFeriados.calcular_feriados import CalcularFeriado
from Projetos.ClassificadorDeSenha.classificar_senha_bianca import ClassificarSenha
from Projetos.ConverteRomano.converte_romano_bianca import ConverterNumeroParaRomano
from Projetos.CriptografiaDeSenha.criptografia_de_senha_bianca import CriptografiaSenha
from Projetos.DistanciaZeros.conta_zeros_bianca import conta_zeros
from Projetos.GeradorSenha.gerar_senha_bianca import GerarSenha
from Projetos.PuctuationCleaner.puctuation_cleaner import RemoverPontuacao
from Projetos.TagCleane.tag_cleaner import RemoverTags
from Projetos.ValidarCpf.validarcpf_bianca import ValidarCPF
from Projetos.ValorMoedas.valor_moedas_bianca import ValorMoedas
from Projetos.WordCount.conta_palavras import ContarPalavra

# executar Calcular Feriados
if __name__ == '__main__':
    print('executar Calcular Feriados')
    print(CalcularFeriado().contarFeriados(2020))

# executar Classificar Senha
if __name__ == '__main__':
    print('executar Classificar Senha')
    print(ClassificarSenha().classificar_senha('Dbia209@'))

# executar Converter numeros para romanos
if __name__ == '__main__':
    print('executar Converter numeros para romanos')
    print(ConverterNumeroParaRomano().numero_para_romano(3))

# executar Criptografia de senha
if __name__ == "__main__":
    print('executar Criptografia de senha')
    print(CriptografiaSenha().hash_md5('bianca'))
    print(CriptografiaSenha().hash_sha256('bianca'))

# executar Cotar Zeros
if __name__ == '__main__':
    print('executar Cotar Zeros')
    print(conta_zeros("0000hduhqwdiuhwqu, 13000000+"))

# executar Gerar Senhas
if __name__ == '__main__':
    print('executar Gerar Senhas')
    print(GerarSenha().gerar_senha())

# executar Remover pontuação
if __name__ == '__main__':
    print('executar Remover pontuação')
    # seu caminho ate o arquivo
    path = ''
    print(RemoverPontuacao().remova_puct("{}/Projetos/PuctuationCleaner/texto.txt".format(path)))

# executar Tag Clear
if __name__ == '__main__':
    print('executar Tag Clear')
    path = ''
    print(RemoverTags().remove_tags('{}/Projetos/TagCleane/htmls/html.txt'.format(path)))

# executar validar CPF
if __name__ == '__main__':
    print('executar validar CPF')
    print(ValidarCPF().valida_cpf("395.567.239.09"))


# executar Valor Moeda
if __name__ == '__main__':
    print('executar Valor Moeda')
    print(ValorMoedas().valor_moeda(10.26))

# executar WordCount
if __name__ == '__main__':
    print('executar WordCount')
    # seu caminho ate o arquivo
    path = ''
    print(ContarPalavra().conta_palavras("{}/Projetos/WordCount/texto.txt".format(path)))

