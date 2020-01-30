import html2text

def remove_tags(txt):

    htmlTexto = txt

    # estânciado a classe do Html2Text
    html = html2text.HTML2Text()

    # tirando todas as tags que contem links e link de imagens
    html.ignore_links = True
    html.ignore_images = True

    # lendo o html com as tags e tirando
    html = html.handle(htmlTexto)

    listaPalavras = html.split()

    if len(listaPalavras) == 0:
        return "Texto Vazio"

    # tirando algum tipo de formatação que não seja pontuação
    html = html.strip().replace('\n', ' ').replace('*', '').replace(' \+', '').replace(' \-', '')

    return html
