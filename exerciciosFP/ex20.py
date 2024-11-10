import os
os.system('cls')

quantidade = int(input("Digite a quantidade de produtos vendidos no dia: "))
pesos = []

for i in range(quantidade):
    pesos.append(float(input("Digite o peso do produto:")))
print("A media dos pesos foi:",sum(pesos)/len(pesos))
print("O maior peso foi:",max(pesos))
print("O menor peso foi:",min(pesos))
print("O total arrecadado foi: R$",sum(pesos)*4.35)