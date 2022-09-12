def função(dia, mes, ano):
    data = 0

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if dia <= 31:
            data = 1
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if dia <= 30:
            data = 1
    if mes == 2:
        if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):
            if(dia <= 29):
                data = 1
        elif(dia <= 28):
            data = 1
    mes -= 1
    mes1 = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
            'jul', 'ago', 'set', 'out', 'nov', 'dez']
    if mes >= 13:
        return print('Mês inválida')
    if (data == 1):
        return print("Nome", ",", dia, 'de ', mes1[mes], 'de', ano)
    else:
        return print('Data inválida')


dia = int(input('informe o dia - '))
mes = int(input('informe o mes - '))
ano = int(input('informe o ano - '))
função(dia, mes, ano)
