import random
numero_max = 10
acertou = False
tentativas = 3
aumenta_nivel = "s"

def jogar (tentativas,acertou):
    numero_secreto = random.randint(1,numero_max)
    print(f"Tente adivinhar o número entre 1 e {numero_max}.")
    print(f"Você tem {tentativas} tentativas.\n")

    while tentativas > 0:
        chute = int(input("Digite um número: "))
        if chute == numero_secreto:
            print("🎉 Parabéns! Você acertou o número!")
            acertou = True
            break
        elif chute < numero_secreto:
            print("Chutou baixo!")
        else:
            print("Chutou alto!")
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}\n")

    if not acertou:
        print("😢 Suas tentativas acabaram.")
        print(f"O número secreto era: {numero_secreto}")
    return acertou

print("🎮 Bem-vindo ao Jogo de Adivinhação!")
acertou = jogar(tentativas,acertou)
if acertou:
    aumenta_nivel = input("Quer aumentar o nível (s/n)? ").lower()
    while aumenta_nivel != "s" and aumenta_nivel != "n":
        aumenta_nivel = input("Inválido! Quer aumentar o nível (s/n)? ").lower()
    if aumenta_nivel == "s":
        numero_max = 50
        tentativas = 7
        acertou = jogar(tentativas,acertou)
        if acertou:
            aumenta_nivel = input("quer aumenta o nível denovo (s/n)? ").lower()
            while aumenta_nivel != "s" and aumenta_nivel != "n":
                aumenta_nivel = input("Inválido! Quer aumentar o nível (s/n)? ").lower()
            if aumenta_nivel == "s":
                numero_max = 100
                tentativas = 9
                acertou = jogar(tentativas,acertou)
                if acertou:
                        aumenta_nivel = input("quer aumenta o nível mais ainda (s/n)? ").lower()
                        while aumenta_nivel != "s" and aumenta_nivel != "n":
                            aumenta_nivel = input("Quer aumentar o nível (s/n)? ").lower()
                        if aumenta_nivel == "s":
                            numero_max = 150
                            tentativas = 12
                            acertou = jogar(tentativas,acertou)
                            if acertou:
                                print("Você é muito bom!")

print("Obrigado por jogar")