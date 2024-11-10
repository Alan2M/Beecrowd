import os
os.system('cls')

matriz = [] * 10
tamanho = 10

for i in range(tamanho):
    for j in range(tamanho):
        matriz[i].append(int(input(f"Digite um numero da posição [{i} {j}] : ")))

for i in range(tamanho):
    for j in range(tamanho):
        print(f"[{matriz[i][j]}]", end="")
    print()