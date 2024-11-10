import os
os.system('cls')

def lim(inferior,superior,lista):
    lista = []

    for i in range(10):
        if i >= inferior and i <= superior:
            lista.append(i)
    return lista
lista = []
for i in range(10):
    i = int(input("Digite um numero"))
inferior = int(input())
superior = int(input())

print(lim(superior,inferior,lista))