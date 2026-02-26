#Programa de classificação de idade
idade = int(input("Digite sua idade: "))

if idade <13:
    print("Você está na categoria: Criança.")
elif idade <17:
    print("Você está na categoria: Adolescente.")
elif idade <59:
    print("Você está na categoria: Adulto.")
else:
    print("Você está na categoria: Idoso.")