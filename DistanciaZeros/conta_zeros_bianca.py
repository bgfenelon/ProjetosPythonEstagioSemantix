
import re

def conta_zeros(texto):

    lista_zero = re.findall("0+",texto)
    return len(max(lista_zero))


if __name__=="__main__":
    try:
        x = conta_zeros("0000hduhqwdiuhwqu, 13000000+")
        print(x)
    except TypeError:
        print ("Função não recebe campos vazios")




