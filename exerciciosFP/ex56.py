import os
os.system('cls')

lista = []
menor = 0
maior = 0
igual = 0

try:
    for i in range(10):
        n = int(input("Digite um numero inteiro:"))
        lista.append(n)
    for i in range(1,10):
        if lista[i] > lista[0]:
            maior += 1
        elif lista[i] < lista[0]:
            menor += 1
        elif lista[i] == lista[0]:
            igual += 1
    print(f"Maiores:{maior}\nMenores:{menor}\nIguais:{igual}")
except ValueError:
    print("")