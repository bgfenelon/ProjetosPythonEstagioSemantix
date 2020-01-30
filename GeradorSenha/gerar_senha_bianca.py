
import random


def gerar_senha():

    numeros = random.randrange(20)
    list_senha = []
    numero = []
    count = 100
    for x in range(numeros):

        letras = random.choice('abcdefghijklmnop')
        number_generate = letras + str(random.randint(0, count * 5)) + letras + str(random.randint(0, count * 39))
        list_senha.append(number_generate)

    if number_generate.count('') < 8:
        print('senha invalida')
        return 0

    for x in number_generate:
        if x.isnumeric():
            numero.append(x)

    if len(numero) == 0:
        print('senha invalida')
        return 0



    return number_generate



if __name__=='__main__':
    print(gerar_senha())













