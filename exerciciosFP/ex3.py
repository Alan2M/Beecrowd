import os
os.system('cls')

carros_vendidos = int(input("Digite quantos carros foram vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = float(input("Digite o valor do salario fixo: "))
comissao = float(input("Digite o valor da comissao para cada carro: "))

salario_final = salario_fixo + comissao*carros_vendidos + valor_vendas*0.05

print("O salario final foi:",salario_final)