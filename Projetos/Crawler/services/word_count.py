from operator import itemgetter

def conta_palavras(txt):
    contarPalavras = dict()
    listaWordCount = []

    texto = txt

    # passando o texto inteiro para letras minusculas
    # e separando as palavras em uma lista
    texto = texto.lower()
    listaPalavras = texto.split()

    # percorrenco cada palavra
    for palavras in listaPalavras:

        # se caso a palavra já esteja na lista adicionar + 1
        if palavras in contarPalavras:
            contarPalavras[palavras] += 1
        else:
            contarPalavras[palavras] = 1

    # adicionar o dict das palavras em listas tuplas ordenado do maior para o o menor pelo intem do dicionario
    listaWordCount = sorted(contarPalavras.items(), key=itemgetter(1), reverse=True)

    return listaWordCount
