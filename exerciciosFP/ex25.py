import os
os.system('cls')

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite um numero da posição [{i} {j}] : ")))

for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end="")
    print()