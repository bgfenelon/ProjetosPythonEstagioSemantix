
def classificar_senha(pwd):

    if type(pwd) != str:
        print("Tipo de senha inválido !")
        return False

    senha = pwd.count("")
    numero = []
    maiusculo = []

    for x in pwd:
        if x.isnumeric():
            numero.append(x)
        if x.isupper():
            maiusculo.append(x)

    if senha >= 8 and len(numero) > 0 and len(maiusculo) > 0:
        print('forte')
        return 2
    if senha >= 8 and len(numero) > 0:
        print('media')
        return 1
    if senha < 8 or len(numero) == 0:
        print('fraca')
        return 0

    print(senha)


if __name__=="__main__":
    try:
        classificar_senha("senhaddhhhjkyt65")
    except TypeError:
        print ("Função não recebe campos vazios")