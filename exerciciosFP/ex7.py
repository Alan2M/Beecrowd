import os
os.system('cls')

idade = int(input("Digite a sua idade:"))

if idade<4 or idade>60:
    ingresso = "Entrada gratuita"
elif idade>=4 and idade<=17:
    ingresso = "20 Reais"
else:
    ingresso = "30 Reais"
print("O valor do ingresso é:", ingresso)