def conversao(valor1, valor2):
    if valor2 > valor1:
        try:
            z = valor2*1.0/valor1
            tratar = round(z, 2)*100
            valor = str(tratar)+"%"
            return valor
        except ZeroDivisionError:
            print(" Oops! Não é possível dividir por 0.")
            exit(0)
    elif valor2 == valor1:
        valor = "0%"
        return valor
    else:
        try:
            z = valor1*1.0/valor2
            tratar = (z-1.0)*100
            valor = str(round(tratar, 0))+"%"
            return valor
        except ZeroDivisionError:
            print(" Oops! Não é possível dividir por 0.")
            exit(0)


x = int(input("Valor 1: "))

y = int(input("Valor 2: "))


print(conversao(x, y))
