def remova_stopwords(txt):

    listaPalvrasSeparadas = []

    if type(txt) != str:
        return 0
    texto = txt

    texto = texto.lower()
    listaPalavrasStopWords = ['eram', 'mesmo', 'tenha', 'nossos', 'nas', 'sejamos', 'aquele', 'meus', 'mais', 'pelo',
                              'teus', 'até', 'esteja', 'houveram', 'tenham', 'eu', 'seriam', 'sua', 'ao',
                              'hão', 'já', 'tenho', 'essa', 'esta', 'tivesse', 'só', 'haja', 'sejam', 'suas',
                              'vocês', 'foram', 'nosso', 'estiver', 'teria', 'lhe', 'essas', 'houveria', 'esteve',
                              'você', 'seu', 'deles', 'tuas', 'um', 'elas', 'houverei', 'pela', 'tínhamos', 'minha',
                              'estivéramos', 'nos', 'de', 'este', 'formos', 'minhas', 'nossas', 'será', 'estiverem',
                              'aqueles', 'teremos', 'estivemos', 'pelas', 'também', 'estivessem', 'nem', 'tivessem',
                              'às', 'à', 'estivermos', 'do', 'esses', 'estavam', 'por', 'pelos', 'dele', 'há', 'como',
                              'na', 'houvemos', 'tivermos', 'as', 'seria', 'tiver', 'estiveram', 'eles', 'das', 'sem',
                              'foi', 'temos', 'lhes', 'terá', 'tua', 'tivemos', 'ela', 'era', 'teu', 'aos', 'num',
                              'seus', 'estejam', 'ou', 'hajam', 'dela', 'quando', 'houvéramos', 'tinham', 'seríamos',
                              'houvessem', 'houve', 'terão', 'fôssemos', 'mas', 'vos', 'tem', 'fora', 'tivéramos',
                              'estes', 'forem', 'são', 'e', 'seremos', 'serão', 'teve', 'dos', 'meu', 'fôramos',
                              'tenhamos', 'aquilo', 'uma', 'isto', 'para', 'hajamos', 'se', 'me', 'tive', 'aquelas',
                              'estava', 'hei', 'fossem', 'que', 'com', 'estão', 'éramos', 'entre', 'quem', 'houverem',
                              'fui', 'estivera', 'os', 'da', 'houvéssemos', 'teríamos', 'é', 'em', 'estas', 'depois',
                              'estamos', 'no', 'o', 'for', 'houverão', 'delas', 'nós', 'seja', 'fosse', 'serei',
                              'estivesse', 'tu', 'houvera', 'não', 'sou', 'aquela', 'houver', 'isso', 'está', 'tiveram',
                              'teriam', 'tivéssemos', 'esse', 'a', 'estou', 'havemos', 'houvesse', 'nossa', 'estive',
                              'numa', 'houveremos', 'estejamos', 'fomos', 'houveriam', 'te', 'tinha', 'tiverem',
                              'estávamos', 'qual', 'houvermos', 'ele', 'houverá', 'terei', 'houveríamos', 'somos',
                              'estivéssemos', 'tém', 'tivera', 'muito']



    listaPalavra = texto.split()

    if len(listaPalavrasStopWords) < len(listaPalavra):
        tirar_palavras = listaPalavrasStopWords
    elif len(listaPalavra) < len(listaPalavrasStopWords):
        tirar_palavras = listaPalavra

    for x in range(len(tirar_palavras)):
        if listaPalavra[x] not in listaPalavrasStopWords:
            listaPalvrasSeparadas.append(listaPalavra[x])

    results = ' '.join(listaPalvrasSeparadas)

    return results