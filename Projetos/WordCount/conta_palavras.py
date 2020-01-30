from operator import itemgetter


class ContarPalavra:

    def conta_palavras(self, txt):
        contarPalavras = dict()
        try:
            if type(txt) == list:
                for i in txt:
                    with open(i) as tx:
                        texto = tx.read()

            else:
                with open(txt) as tx:
                    texto = tx.read()
        except FileNotFoundError:
            return "Arquivo não existe"

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

