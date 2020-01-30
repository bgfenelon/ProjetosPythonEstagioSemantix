import random
import hashlib as hs
import re


# conversão de números romanos

def valida_numero_romano (numero):
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


############################################################

# validação de cpfs

def retira_formatacao_cpf(num_cpf):
    list_form = []
    if type(num_cpf) != str:
        #print("Tipo de CPF invalido !")
        return 0
    for x in num_cpf:
        if x.isnumeric():
            list_form.append(x)
    juntar_num = ''.join(list_form)
    return juntar_num

def valida_cpf(num_cpf):
    if num_cpf == 0:
        #print("Tipo de CPF invalido !")
        return 0
    list_num = []
    list_repetidos = []
    tam = len(num_cpf)
    if tam == 11:
        for i in num_cpf:
           list_num.append(i)
        for x in list_num:
            if x == i :
                list_repetidos.append(x)
        if len(list_repetidos) == 11:
            #print("Numeros repetidos CPF inválido !")
            return "CPF inválido"
        return num_cpf,'CPF Válido'

    elif tam > 11:
        #print("CPF invalido !")
        return "CPF inválido !"
    else:
        #print("CPF imcompleto !")
        return "CPF imcompleto !"


# distancia de zeros
def conta_zeros(texto):
    lista_zero = re.findall("0+",texto)

    return texto,len(max(lista_zero))


# gerador de senhas
def gerar_senha():
    numeros = random.randrange(20)
    list_senha = []
    numero = []
    count = 100
    for x in range(numeros):
        letras = random.choice('abcdefghijklmnop')
        number_generate = letras + str(random.randint(0, count * 5)) + letras + str(random.randint(0, count * 2339)) + letras
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



# classificador de senhas
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
        clas = 'forte'
        return 2, clas
    if senha >= 8 and len(numero) > 0:
        clas = 'média'
        return 1, clas
    if senha < 8 or len(numero) == 0:
        clas = 'fraca'
        return 0, clas

    return senha


# hash no endpoint

def hash_md5(pwd):

    if type(pwd) != str:
        print("Tipo de senha inválido !")
        return 0

    md5 = hs.md5(pwd.encode('utf-8')).hexdigest()
    return md5


def hash_sha256(pwd):

    if type(pwd) != str:
        print("Tipo de senha inválido !")
        return 0

    sha256 = hs.sha256(pwd.encode('utf-8')).hexdigest()
    return sha256

#
# if __name__ == "__main__":
#
#     x = conta_zeros("rdf0000wsdrt00000d0w0e0r000g00f0d00000")
#     print(x)