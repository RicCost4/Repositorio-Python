from random import *


print("Foi gerado um numero de 1 há 100.")
print("tente adivinhar qual esse numero, você tem varias tentativas")

x = randint(1, 100)
opcao = 0
cont = 0
listaNumeros = []
while(True):
    opcao = int(input("Adivinhe o numero: "))
    if opcao < x:

        print("\nNumero errado, maior")
    elif opcao > x:

        print("\nNumero errado, menor")
    elif opcao == x:
        print("\nVoce acertou o numero, meus parabens.")
        break
    cont += 1
    listaNumeros.append(opcao)

print("Numeros Digitados: " + str(listaNumeros))
print("numero sorteado =", str(x))
print("Numeros de tentativas =", str(cont))
