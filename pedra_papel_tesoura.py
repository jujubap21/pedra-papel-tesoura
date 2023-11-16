import random


print("********************************************")
print("Bem vindo ao jogo de Pedra, Papel, Tesoura!".upper())
print("-------------------------------------------- \nEscolha uma opção: \n[0]Pedra \n[1]Papel \n[2]Tesoura \n--------------------------------------------")
pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']

cpu = random.choice(pedra_papel_tesoura)

jogador=int(input("Digite a sua jogada: \n********************************************"))

if cpu == "pedra":
    print("O oponente escolheu: Pedra")
    if jogador == 0:
        print("Empatou! Os dois escolheram pedra.")
    elif jogador == 1:
        print("Você venceu! Papel embrulha pedra.")
    elif jogador == 2:
        print("Você perdeu! Pedra quebra tesoura.")
    else:
        print("Digite '1', '2' ou '3'.")

elif cpu == "papel":
    print("O oponente escolheu: Papel")
    if jogador == 0:
        print("Você Perdeu! Papel embrulha pedra.")
    elif jogador == 1:
        print("Empatou! Os dois escolheram papel.")
    elif jogador == 2:
        print("Você venceu! Tesoura corta papel.")
    else:
        print("Digite '1', '2' ou '3'.")
            
elif cpu == "tesoura":
    print("O oponente escolheu: Tesoura")
    if jogador == 0:
        print("Você venceu! Pedra quebra tesoura.")
    elif jogador == 1:
        print("Você perdeu! Tesoura corta papel.")
    elif jogador == 2:
        print("Empatou! Os dois escolheram tesoura!")
    else:
        print("Digite '1', '2' ou '3'.")
else:
    print("Digite '1', '2' ou '3'.")

reiniciar = input("******************************************** \nVocê quer jogar de novo? Digite 'sim' ou 'não'.")
        
while (reiniciar == "sim"):
    print("********************************************")
    print("-------------------------------------------- \nEscolha uma opção: \n[0]Pedra \n[1]Papel \n[2]Tesoura \n--------------------------------------------")
    pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']

    cpu = random.choice(pedra_papel_tesoura)

    jogador=int(input("Digite a sua jogada: \n********************************************"))

    if cpu == "pedra":
        print("O oponente escolheu: Pedra")
        if jogador == 0:
            print("Empatou! Os dois escolheram pedra.")
        elif jogador == 1:
            print("Você venceu! Papel embrulha pedra.")
        elif jogador == 2:
            print("Você perdeu! Pedra quebra tesoura.")
        else:
            print("Digite '1', '2' ou '3'.")

    elif cpu == "papel":
        print("O oponente escolheu: Papel")
        if jogador == 0:
            print("Você Perdeu! Papel embrulha pedra.")
        elif jogador == 1:
            print("Empatou! Os dois escolheram papel.")
        elif jogador == 2:
            print("Você venceu! Tesoura corta papel.")
        else:
            print("Digite '1', '2' ou '3'.")
            
    elif cpu == "tesoura":
        print("O oponente escolheu: Tesoura")
        if jogador == 0:
            print("Você venceu! Pedra quebra tesoura.")
        elif jogador == 1:
            print("Você perdeu! Tesoura corta papel.")
        elif jogador == 2:
            print("Empatou! Os dois escolheram tesoura!")
        else:
            print("Digite '1', '2' ou '3'.")
    else:
        print("Digite '1', '2' ou '3'.")

    reiniciar = input("Você quer jogar de novo? Digite 'sim' ou 'não'.")

    if reiniciar == "não":
        break