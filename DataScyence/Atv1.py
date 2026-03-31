nome = input("Digite seu nome: ")
print(nome)

idade = int(input("Digite sua idade: "))
if idade < 18:
    print(f"Você tem {idade} anos, portanto é menor de idade!")
else:
    print(f"Você tem {idade} anos, portanto é maior de idade!")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
print(f"A soma destes números é: {soma}")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resto = num1 % num2
print(f"O resto da divisão de {num1} por {num2} é: {resto}")

nome = input("Digite seu nome: ")
telefone = int(input("Digite seu telefone: "))
endereco = input("Digite seu endereço: ")
email = input("Digite seu email: ")
cadastro = [nome,telefone,endereco,email]
print(f"Aqui está sua ficha: {cadastro}")