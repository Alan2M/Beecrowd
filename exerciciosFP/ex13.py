import os
os.system('cls')

valor_total = 0
valores = 1
while valores!= 0:
    valores = float(input("Digite os valores:"))
    if valores>0:
        valor_total += valores
if valor_total>1000:
    valor_total = valor_total*0.9
print("Valor total a pagar é: ",valor_total)