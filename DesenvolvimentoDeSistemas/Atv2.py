'''

Crie um programa em Python que:

Gere um número aleatório entre 1 e 50.

Dê ao jogador 5 tentativas para acertar o número.

A cada tentativa:

O jogador deve digitar um número.

O programa deve informar se o número é maior ou menor que o número secreto.

O jogo termina quando:

O jogador acertar o número; ou

As 5 tentativas acabarem.

Ao final, o programa deve mostrar:

Uma mensagem de vitória (se acertar).

Ou o número correto (se perder).

'''
import random
numero_aleatório = random.randint(1,50)
acertou = False
tentativas = 7

print("🎮 Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 50.")
print("Você tem 7 tentativas.\n")

while tentativas > 0:
    chute = int(input("Digite um número: "))
    if chute == numero_aleatório:
        print("🎉 Parabéns! Você acertou o número!")
        acertou = True
        break
    elif chute < numero_aleatório:
        print("Chutou baixo demais!")
    else:
        print("Chutou alto demais!")
    tentativas -= 1
    print(f"Tentativas restantes: {tentativas}\n")

if not acertou:
    print("😢 Suas tentativas acabaram.")
    print(f"O número secreto era: {numero_aleatório}")