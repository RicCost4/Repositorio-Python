def valorKM(km):
    if(km <= 200):
        valor = 1500
    elif(km > 200 and km <= 300):
        vKm = 7.68
        valor = km*vKm
    elif(km > 300 and km <= 500):
        vKm = 5.76
        valor = km*vKm
    elif(km > 500 and km <= 750):
        vKm = 5.12
        valor = km*vKm
    elif(km > 750 and km <= 1000):
        vKm = 5.19
        valor = km*vKm
    else:
        vKm = 5.18
        valor = km*vKm
    return print(f'O valor aproximado {km}km é R$ {round(valor, 2)}')


numero = int(input('Digite a KM da viajem: '))

valorKM(numero)
