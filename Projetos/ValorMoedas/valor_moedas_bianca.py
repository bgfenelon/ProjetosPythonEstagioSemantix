

def valor_moeda(vlr):

    if vlr == 0:
        return 0
    elif type(vlr) != float:
        return 0

    numeros = [1,0.5,0.25,0.10,0.05,0.01]
    moedas = [" R$ 1,00"," R$ 0,50"," R$ 0,25"," R$ 0,10"," R$ 0,05"," R$ 0,01"]


    lista_moedas = []
    i = 0

    while(vlr > 0):
        vlr = round(vlr,2)
        # veficando numero existente

        if(vlr >= numeros[i]):
            #adicionando na lista
            lista_moedas.append(moedas[i])
            # percorrendo a lista
            vlr -= numeros[i]
        else:
            i += 1


    junt_elems = ''.join(lista_moedas)





    moedas = {

        "1_real": lista_moedas.count(" R$ 1,00"),
        "50_centavos":lista_moedas.count(" R$ 0,50"),
        "25_centavos":lista_moedas.count(" R$ 0,25"),
        "10_centavos":lista_moedas.count(" R$ 0,10"),
        "5_centavos":lista_moedas.count(" R$ 0,05"),
        "1_centavos":lista_moedas.count(" R$ 0,01")
    }

    return moedas


if __name__== '__main__':
    x = valor_moeda(10.26)
    print(x)













