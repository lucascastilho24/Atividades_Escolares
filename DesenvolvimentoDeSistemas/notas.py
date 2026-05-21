notas = []
numero_de_notas = int(input('Qual é o número de notas? '))
for i in range(0,numero_de_notas):
    nota = float(input('Digita a nota: '))
    notas.append(nota)

print(f'As notas são: {notas}')
media = sum(notas)/numero_de_notas
print(f'A média é: {media}')
if media == 10:
    print('Um ótimo aluno!')
elif media >= 8:
    print('Um bom aluno!')
elif media >= 6:
    print('Ficou na média!')
elif media >= 1:
    print('Está abaixo da média!')
else:
    print('Zerou em tudo!')