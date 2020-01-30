import sys
import requests
import bs4

from Projetos.Crawler.services.tag_clear import remove_tags
from Projetos.Crawler.services.puctuation_cleaner import remova_puct
from Projetos.Crawler.services.remove_stopwords import remova_stopwords
from Projetos.Crawler.services.word_count import conta_palavras

txt = sys.argv[1:]

def crawler(link):

    if link == "":
        return "Link Vazio"

    if type(link) == list:
        for i in link:
            link = i

    listaImagens = []
    listaDezprimeiros = []

    try:
        # pega o link da requisição e passa para o soup
        html = requests.get(link).text
        soup = bs4.BeautifulSoup(str(html),'html.parser')

        # e da biblioteca soup os links das imagens
        for img in soup.find_all('img'):
            # faz o get de  uma lista de links de imagens
            pegandoImagensPagina = img.get('data-src', img.get('dfr-src'))

            # adiciona na lista os links que não estiver em None
            if pegandoImagensPagina is not None:
                listaImagens.append(pegandoImagensPagina)


        # faz toda a limpeza de pontuação stopwords ...
        removendoTag = remove_tags(html)
        removendoPontuacao = remova_puct(removendoTag)
        removendoStopWords = remova_stopwords(removendoPontuacao)
        contarPalavras = conta_palavras(removendoStopWords)

        #adiciona só os dez primerios
        for x in range(10):
            listaDezprimeiros.append(contarPalavras[x])

        # retorna a lista de palavras dos dez primeiros que mais aparecem e a primeira imagem do site
        print(listaDezprimeiros)
        print(listaImagens[0])
        return listaDezprimeiros, listaImagens[0]
    except IndexError:
        return "Link Não Existe"
    except requests.exceptions.MissingSchema:
        return "Link Não Existe"


if __name__ == '__main__':
    a,b = crawler('https://veja.abril.com.br/mundo/jeanine-anez-diz-que-anunciara-novas-eleicoes-bolivianas-em-breve/')

