def soma(x):
    return x + 1


c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0

while(True):
    cont = print("Urna: [1]Canditato 1" + "/n" + "[2]Canditato 2" + "/n" + "[3]Canditato 3" +
                 "/n" + "[4]Canditato 4" + "/n" + "[5]Voto Nulo" + "/n" + "[6]Voto Branco" + "/n" + "[0]Sair")
    opcao = input("Digite a OPÇÃO: ")

    if opcao == "1":
        c1 = soma(c1)
    elif opcao == "2":
        c2 = soma(c2)
    elif opcao == "3":
        c3 = soma(c3)
    elif opcao == "4":
        c4 = soma(c4)
    elif opcao == "5":
        vn = soma(vn)
    elif opcao == "6":
        vb = soma(vb)
    elif opcao == "0":
        break
    elif opcao == '':
        print("Digite uma valor")
    else:
        print("Valor invalida!!")
print("Canditato 1 Votos [" + str(c1) + "]")
print("Canditato 2 Votos [" + str(c2) + "]")
print("Canditato 3 Votos [" + str(c3) + "]")
print("Canditato 4 Votos [" + str(c4) + "]")
print("Votos Nulos [" + str(vn) + "]")
print("Votos em Brancos [" + str(vb) + "]")
