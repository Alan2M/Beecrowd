import os
os.system('cls')

pares = []
impares = []
lista = []

for i in range (10):
    n = int(input("Digite um numero:"))
    lista.append(n)
for i in range(10):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    if lista[i] % 2 != 0:
        impares.append(lista[i])
print(lista)
print(pares)
print(impares)