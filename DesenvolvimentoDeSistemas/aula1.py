nome=input("Digite seu nome: ")
try:
    anoNascimento=int(input("Digite seu ano de nascimento: "))
    idade=2026-anoNascimento
    print(f"Olá, {nome}! Você tem aproximadamente {idade} anos.")
except:
    print("As informações inseridas são inválidas!")