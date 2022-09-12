from translate import Translator

# configura a tradução
# tradução ingles p/ portugues.
i_p = Translator(from_lang="english", to_lang="pt-br")
# tradução ingles p/ espanhol.
i_s = Translator(from_lang="english", to_lang="spanish")
# tradução espanhol p/ portugues.
s_p = Translator(from_lang="spanish", to_lang="pt-br")
# tradução espanhol p/ ingles.
s_i = Translator(from_lang="spanish", to_lang="english")
# tradução portugues p/ ingles.
p_i = Translator(from_lang="pt-br", to_lang="english")
# tradução portugues p/ espanhol.
p_s = Translator(from_lang="pt-br", to_lang="spanish")

while True:
    opc = int(
        input("Deseja traduzir qual lingua: \n\t1 -- Ingles\n\t2 -- Espanhol.\n\t3 -- Portugues.\nDigite o numero correspondente:  "))

    if opc == 1:  # condição da tradução do ingles.
        ing = int(input(
            "Deseja traduzir\n\t1 -- Inglês p/ Portugês.\n\t2 -- Inglês p/ Espanhol\nDigite o numero correspondente:  "))

        if ing == 1:
            frase = input("Escrita em Ingles: ")
            tra_i_p = i_p.translate(frase)

            print("Tradução:", tra_i_p)
        if ing == 2:
            frase = input("Escrita em Ingles: ")
            tra_i_s = i_s.translate(frase)

            print("Tradução:", tra_i_s)

    if opc == 2:  # condição da tradução do espanhol.
        esp = int(input(
            "Deseja traduzir\n\t1 -- Espanhol p/ Portugês.\n\t2 -- Espanhol p/ Inglês\nDigite o numero correspondente:  "))
        if esp == 1:
            frase = input("Escrita em Espanhol: ")
            tra_s_p = s_p.translate(frase)

            print("Tradução:", tra_s_p)
        if esp == 2:
            frase = input("Escrita em Espanhol: ")
            tra_s_i = s_i.translate(frase)

            print("Tradução:", tra_s_i)

    if opc == 3:  # condição da tradução do portugues.
        pot = int(input(
            "Deseja traduzir\n\t1 -- Português p/ Inglês.\n\t2 -- Português p/ Espanhol\nDigite o numero correspondente:  "))
        if pot == 1:
            frase = input("Escrita em Português: ")
            tra_p_i = p_i.translate(frase)

            print("Tradução:", tra_p_i)
        if pot == 2:
            frase = input("Escrita em Português: ")
            tra_p_s = p_s.translate(frase)

            print("Tradução:", tra_p_s)

    cont = input("Deseja Continuar a traduzir:\n\tSim.\n\tNão.\n: ")
    # condição da continuação do while.
    if cont == "Não" or cont == "não" or cont == "nao" or cont == "NAO" or cont == "NÃO" or cont == "Nao":
        print("Fim do Programa....")
        break
