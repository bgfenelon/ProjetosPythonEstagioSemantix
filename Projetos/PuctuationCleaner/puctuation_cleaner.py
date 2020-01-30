import sys

txt = sys.argv[1:]


def remova_puct(txt):
    if type(txt) != str:
        return 0

    try:
        if type(txt) == list:
            for i in txt:
                print(i)
                with open(i) as tx:
                    texto = tx.read()
        else:
            with open(txt) as tx:
                texto = tx.read()
    except FileNotFoundError:
        return "Arquivo não existe"

    texto = texto.lower()
    quebrandoTexto = texto.strip().replace(",", "").replace("/","").replace("{","").replace("}","")\
        .replace("?", "").replace("!", "").replace(":", "").replace(":", "") \
        .replace("...", "").replace('"', "").replace("-", "").replace(".","") \
        .replace("(", "").replace(")", "").replace("—", "").replace("'", "").replace("_", "").replace("#", "")


    return quebrandoTexto


if __name__ == '__main__':
    x = remova_puct("texto.txt")
    print(x)
