while True:
    cpf = input('Qual CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    if len(cpf) != 11:
        print('Invalido, tem que ter 11 digitos')

    elif not cpf.isnumeric():
        print('Digite apenas números')
    else:
        for i in range(19):
            if i > 8:
                i -= 9

            total += int(novo_cpf[i]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                digito = 11 - (total % 11)

                if digito > 9:
                    digito = 0
                total = 0
                novo_cpf += str(digito)

        if cpf == novo_cpf:
            print('Valido')
        else:
            print('Invalido')