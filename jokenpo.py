from random import choice
import time
print(f"\n{'-'*10} Vamos jogar jokenpo!{'-'*10}\n  ")
entrar = int(input("""Comecar jogo?
1 - sim
2 - sair
>"""))

while True:

    if entrar == 1:
        opcoes = ["pedra", "papel", "tesoura"]
        utilizador = int(input("""\nEscolha:
1 - Pedra
2 - Papel
3 - Tesoura
4 - sair do jogo
>"""))
        pc = choice(opcoes)
        print("\nAguarde...\n")
        time.sleep(2)
        if (utilizador == 1 and pc == "pedra") or \
                (utilizador == 2 and pc == "papel") or \
                (utilizador == 3 and pc == "tesoura"):
            print("Empate!")
        elif (utilizador == 1 and pc == "tesoura") or \
                (utilizador == 2 and pc == "pedra") or \
                (utilizador == 3 and pc == "papel"):
            print("Voce ganhou!")
        elif utilizador == 4:
            print("Obrigada por jogar!")
            break

        else:
            print("Voce perdeu!")

        if utilizador == 1:
            utilizador = "pedra"
        elif utilizador == 2:
            utilizador = "papel"
        elif utilizador == 3:
            utilizador = "tesoura"
        else:
            print("Opcao Invalida, tente outra vez!")
        print(f"""O computador escolheu: {pc}
        Voce escolheu: {utilizador}""")


    elif entrar == 2:
        print("Obrigada por jogar!")
        break


