from datetime import date
import sys



def calculandoPascoa(ano):
    # Calculando as Pascoa
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    mes = (h + L - 7 * m + 114) // 31
    dia = 1 + (h + L - 7 * m + 114) % 31

    return mes,dia

def contarFeriados(ano):
    if type(ano) != int:
        return 0
    elif ano < 1850 or ano > 2209:
        return "Ano não existe"

    mesPascoa,diaPascoa = calculandoPascoa(ano)

    # Especificando o ano mes e dia em que a data ira começar
    pascoa = date(ano,mesPascoa,diaPascoa)

    # metodo fromordinal retorna a data de acordo com o Calendario Gregoriano onde recebe o "Ordinal"
    # o metodo pascoa.toordinal() conta os dias percorridos desdo ano  1/1/0001 ele fornece o total de dias
    # até a data determinada que nesse caso e a pascoa de um determinado ano
    carnaval = date.fromordinal(pascoa.toordinal() - 47)
    sexta_feira_santa = date.fromordinal(pascoa.toordinal() - 2)
    corpusChristi = date.fromordinal(pascoa.toordinal() + 60)

    sfs = sexta_feira_santa
    cc = corpusChristi

    json_data_feriados = {
                "carnaval ":"{}/{}/{}".format(carnaval.day,carnaval.month,carnaval.year),
                "sexta_feira_santa":"{}/{}/{}".format(sfs.day,sfs.month,sfs.year),
                "pascoa":"{}/{}/{}".format(pascoa.day,pascoa.month,pascoa.year),
                "corpus_christi":"{}/{}/{}".format(cc.day,cc.month,cc.year)
                }


    return json_data_feriados

if __name__ == '__main__':
    ano = int(sys.argv[1])
    d = contarFeriados(ano)
    print(d)
