def validar_cpf():
    cpf = []
    entrada = input("Digite seu CPF: ")
    for i in entrada:
        cpf.append(int(i))

    dv = cpf[-2:]
    part1 = cpf[:9]

    def calculo_dro_digito(part,peso):
        soma = []
        if peso == 10:
            for i in part:
                soma.append(int(i)*peso)
                peso -= 1
        else:
            part.append(digito1)
            for i in part:
                soma.append(int(i)*peso)
                peso -= 1

        resto = sum(soma) % 11
        return 0 if resto < 2 else 11- resto

    digito1 = calculo_dro_digito(part1,10)
    digito2 = calculo_dro_digito(part1,11)
    if dv[0] == digito1 and dv[1] == digito2:
        print(f"O CPF {entrada} é válido!")
    else:
        print("O CPF é inválido!")
validar_cpf()