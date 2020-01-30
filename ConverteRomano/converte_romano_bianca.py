import  traceback



def valida_numero (numero):


    if type(numero) != int:
        return 0

    try:
        if (numero > 0  and  numero <= 4000):
            return numero
        else:
            #print("Numero maior que 3000 ou menor/igual que 0 ",numero)
            return 0
    except TypeError:
        #print('Tipo do valor não esperado ',type(numero))
        return 0






def numero_para_romano(num):

    if num == 0:
        return 0
    #
    #
    # # moedas = {
    # #
    # #     "1_real": v,
    # #     "50_centavos":v,
    # #     "25_centavos":v,
    # #     "10_centavos"v,
    # #     "5_centavos"v,
    # #     "1_centavos": v
    # # }
    #
    # return vlr
    #


    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "I"]

    list_romanos = []
    list_tam = []
    i = 0

    while(num > 0):

        # veficando numero existente
        if(num >= numeros[i]):
            #adicionando na lista
            list_romanos.append(romanos[i])
            # percorrendo a lista
            num -= numeros[i]
        else:
            i += 1


    junt_elems = ''.join(list_romanos)
    return junt_elems




if __name__ == '__main__':
    try:
        numero_para_romano(valida_numero(234))
    except TypeError:
        print ("Função não recebe campos vazios")
