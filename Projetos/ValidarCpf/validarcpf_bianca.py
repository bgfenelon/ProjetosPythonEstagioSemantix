
class ValidarCPF:

    @classmethod
    def retira_formatacao(self,num_cpf):
        list_form = []

        if type(num_cpf) != str or num_cpf == None:
            #print("Tipo de CPF invalido !")
            return 0

        for x in num_cpf:
            if x.isnumeric():
                list_form.append(x)
        juntar_num = ''.join(list_form)
        return juntar_num

    def valida_cpf(self,num_cpf):

        num_cpf = self.retira_formatacao(num_cpf)

        if num_cpf == 0 or num_cpf == None:
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
                return "Numeros repetidos CPF inválido"

            return num_cpf
        elif tam > 11:
            #print("CPF invalido !")
            return "CPF inválido !"
        else:
            #print("CPF imcompleto !")
            return "CPF imcompleto !"
