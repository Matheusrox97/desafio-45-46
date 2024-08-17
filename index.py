import random

def jogada_aleatoria():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)

def play():
    print("Pedra, papel e tesoura!")
    while True:
        player = input("Faça sua jogada! (pedra, papel ou tesoura): ").lower()
        computador = jogada_aleatoria()
        print(f"\nVocê escolheu {player} e o computador escolheu {computador}.\n")

        if player == computador:
            print(f"Empate! Ambos escolheram {player}.")
        elif player == 'pedra':
            if computador == 'tesoura':
                print("Pedra quebra tesoura! Você venceu!")
            else:
                print("Papel enrola na pedra! Você perdeu.")
        elif player == 'papel':
            if computador == 'pedra':
                print("Papel enrola na pedra! Você venceu!")
            else:
                print("Tesoura corta papel! Você perdeu.")
        elif player == 'tesoura':
            if computador == 'papel':
                print("Tesoura corta papel! Você venceu!")
            else:
                print("Pedra esmaga tesoura! Você perdeu.")

        play_again = input("Jogar novamente? (sim/não): ").lower()
        if play_again != 'sim':
            break

play()