import os
os.system('cls')

quantidade = 0
nota = 0
nota_soma = 0

while True:
    nota = float(input("Digite a nota: "))

    if nota == -1:
        break

    quantidade += 1
    nota_soma = nota + nota_soma
media = nota_soma/quantidade
print("A quantidade de notas foram:",quantidade,"\nA media das notas foram: ",media)
