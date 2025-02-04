from random import randint
from time import sleep

print(f"{'-' * 10} Casino {'-' * 10}")
saldo = 100

while True:
    print(f"Saldo atual: {saldo} pontos")
    escolha = int(input("""Escolha um jogo:
1 - Slot Machine
2 - Black Jack
3 - Sair
> """))

    if saldo <= 0:
        print("Voce ficou sem saldo! O jogo acabou.")
        break

    elif escolha == 1:
        if saldo < 10:
            print("Saldo insuficiente para jogar Slot Machine. (minimo de 10 pontos)")
            continue

        print("\nBem vindo a Slot Machine!")
        saldo -= 10
        print("Girando...")
        sleep(2)

        num1 = randint(1, 5)
        num2 = randint(1, 5)
        num3 = randint(1, 5)
        print(f"Resultado: {num1} {num2} {num3}")

        if num1 == num2 == num3:
            print("Parabens! Voce ganhou 100 pontos!")
            saldo += 100
        elif num1 == num2 or num2 == num3 or num1 == num3:
            print("Voce fez um par! Ganhou 5 pontos.")
            saldo += 5
        else:
            print("Nenhum numero igual... Voce perdeu!")

    elif escolha == 2:
        if saldo < 10:
            print("Saldo insuficiente para jogar Black Jack. (minimo de 10 pontos)")
            continue

        print("\nBem vindo ao Black Jack!")
        aposta = int(input("Quanto deseja apostar? (minimo 10 pontos) \n> "))
        if aposta > saldo or aposta < 10:
            print("Aposta invalida!")
            continue

        saldo -= aposta
        jogador_total = randint(2, 10)
        banca_total = randint(2, 10)

        print(f"\nSua carta inicial: {jogador_total}")
        sleep(1)

        while jogador_total < 21:
            compra = int(input("""Comprar outra carta? 
1 - Sim
2 - Nao
> """))
            if compra == 1:
                n_carta = randint(2, 10)
                jogador_total += n_carta
                print(f"Nova carta: {n_carta} (Total: {jogador_total})")
                sleep(1)
                if jogador_total > 21:
                    print("Voce ultrapassou os 21 pontos e perdeu a rodada.")
                    break
            else:
                break

        while banca_total < 17:
            banca_total += randint(2, 10)

        print(f"\nCartas da banca: {banca_total}")
        print(f"Seu total: {jogador_total}")

        if jogador_total > 21 or (21 >= banca_total > jogador_total):
            print("Voce perdeu a sua aposta.")
        else:
            print("Parabens! Voce ganhou!")
            saldo += aposta * 2

    elif escolha == 3:
        print("Obrigado por jogar!")
        break
    else:
        print("Opcao invalida, tente novamente.")
