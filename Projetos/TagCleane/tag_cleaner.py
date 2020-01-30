
import html2text
import sys
txt = sys.argv[1:]

def remove_tags(txt):
	try:
		if type(txt) == list:
			for i in txt:
				with open(i) as tx:
					htmlTexto = tx.read()

		else:
			with open(txt) as tx:
				htmlTexto = tx.read()
	except FileNotFoundError:
		return 'Caminho errado !'

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

if __name__ == '__main__':
	x = remove_tags(txt)
	print(x)

