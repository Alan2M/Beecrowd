import os
os.system('cls')

ano_admissão = int(input("Digite o seu ano de admissão:"))
salario_atual = int(input("Digite seu salário atual:"))
ano_reajuste = int(input("Digite o ano do último reajuste salarial:"))
anos_casa = 2024-ano_admissão

if 2024-ano_reajuste >= 2:
    if anos_casa > 10:
        novo_salario = salario_atual * 1.3
    elif anos_casa > 5 and anos_casa <=10:
        novo_salario = salario_atual * 1.2
    else: 
        novo_salario = salario_atual * 1.1
    print("O novo salario será:", novo_salario)
else:
    print("Não está apto a reajuste salarial!")
