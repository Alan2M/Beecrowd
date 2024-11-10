import os
os.system('cls')

lista = []

n = input("Digite produto para adicionar a lista: ").lower()
lista.append(n)
while True:
    n = input("Digite produto para adicionar a lista: ").lower()
    if n == "sair":
        break
    else:
        if n not in lista:
            lista.append(n)
print(lista)