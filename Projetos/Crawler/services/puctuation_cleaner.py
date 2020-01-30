def remova_puct(txt):
    if type(txt) != str:
        return 0

    texto = txt

    texto = texto.lower()
    quebrandoTexto = texto.strip().replace(",", "").replace("/","").replace("{","").replace("}","")\
        .replace("?", "").replace("!", "").replace(":", "").replace(":", "") \
        .replace("...", "").replace('"', "").replace("-", "").replace(".","") \
        .replace("(", "").replace(")", "").replace("—", "").replace("'", "").replace("_", "").replace("#", "")


    return quebrandoTexto