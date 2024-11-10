import os
os.system('cls')

matriz = [[], [], []]
sc = 0
impares = 0
menor = 100000
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f"Digite um numero da posição [{i} {j}] : ")))
        if matriz[i][j] % 2 != 0:
            impares = impares + matriz[i][j]
        if j == 0:
            sc = sc + matriz[i][j]
        if i == 2:
            if menor > matriz [i][j]:
                menor = matriz[i][j]
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end="")
    print()
print(impares)
print(sc)
print(menor)