import re

def conta_zeros(texto):
    lista_zero = re.findall("0+", texto)
    return len(max(lista_zero))
