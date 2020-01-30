
class ConverterNumeroParaRomano:

    @classmethod
    def valida_numero (self,numero):

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

    def numero_para_romano(self,num):
        num = self.valida_numero(num)

        if num == 0:
            return 0

        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 1]
        romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "I"]

        list_romanos = []
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

