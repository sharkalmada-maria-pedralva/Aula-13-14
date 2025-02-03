
#O teclado do meu computador e ingles por isso nao tem acentos nem C de cedilha

titulo = "QUIZ - Quem quer ser milionário?"
premio = 0

print(f"""{'-'*10} {titulo} {'-'*10}""")

while True:
    entrar = int(input("""Comecar Quiz?
    1 - sim
    2 - sair
    >"""))

    if entrar == 1:
        print("""
Este Quiz tem 5 perguntas.
Cada pergunta vai valer 20.000 euros, acerte todas as perguntas e chegue a 1.000.000 para ganhar.
Vamos comecar!""")
        p1 = int(input("""\nPrimeira pergunta: Qual e a capital de Alemanha?
    1 - Berlim
    2 - Paris
    3 - Darmstadt
    4 - Amsterdam
    >"""))
        if p1 == 1:
            premio += 200000
            print(f"\nVoce acertou! Ate agora tem {premio} euros. Proxima pergunta;")

        else:
            premio = premio - premio
            print("\nVoce errou! A resposta certa era Berlim. Proxima pergunta;")

        p2 = int(input("""Segunda pergunta: Quantos lados tem um dado?
    1 - oito
    2 - quatro
    3 - seis
    4 - cinco
    >"""))
        if p2 == 3:
            premio += 200000
            print(f"\nVoce acertou! Ate agora tem {premio} euros. Proxima pergunta;")

        else:
            premio = premio - premio
            print("\nVoce errou! A resposta certa era seis. Proxima pergunta;")

        p3 = int(input("""Terceira pergunta: O vinho é feito com que fruta?
    1 - banana
    2 - amora
    3 - mirtilo
    4 - uva
    >"""))
        if p3 == 4:
            premio += 200000
            print(f"\nVoce acertou! Ate agora tem {premio} euros. Proxima pergunta;")

        else:
            premio = premio - premio
            print("\nVoce errou! A resposta certa era uva. Proxima pergunta;")

        p4 = int(input("""Quarta pergunta: Quantas casas decimais tem o numero pi?
    1 - tres
    2 - centenas
    3 - milhares
    4 - infinitas
    >"""))
        if p4 == 4:
            premio += 200000
            print(f"\nVoce acertou! Ate agora tem {premio} euros. Proxima pergunta;")

        else:
            premio = premio - premio
            print("\nVoce errou! A resposta certa era infinitas. Proxima pergunta;")

        p5 = int(input("""Quantos dias tem um ano bissexto??
    1 - 366 dias
    2 - 360 dias
    3 - 365 dias
    4 - 600 dias
    >"""))
        if p5 == 1:
            premio += 200000
            print(f"\nVoce acertou! Acabou o quiz com {premio} euros.")

        else:
            premio = premio - premio
            print("\nVoce errou! A resposta certa era 366.")

        if premio == 1000000:
            print(f"{'-'*10}Paraben!! Voce venceu o Quiz! Obrigado por jogar.{'-'*10}")
            

        else:
            premio = premio - premio
            print(f"{'-'*10}Voce nao acertou todas as perguntas, tente denovo!{'-'*10}")




    elif entrar == 2:
        print(f"{'-'*10}Obrigado por jogar!{'-'*10}")
        break

    else:
        print("Opcao invalida, tente outra vez.")
