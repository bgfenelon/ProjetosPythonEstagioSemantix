import sys


def numeros_romanos(numero):


    num_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC':90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000

    }

    tam = len(str(numero))

    if numero < 3000:

        guardar = ''

        if tam == 1:
            for i in num_romanos:
                if numero == num_romanos[i]:
                    print(i)

                vezes = int(numero / num_romanos[i])
                print(vezes)


        elif tam == 2:
            for i in num_romanos:
                if numero == num_romanos[i]:
                    print(i)
        else:
            for i in num_romanos:
                if numero == num_romanos[i]:
                    print(i)


    else:
        print('e maior que 3000')


if __name__ == '__main__':

    numeros_romanos(5)