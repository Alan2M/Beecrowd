import os
os.system('cls')

matriz = [[],[],[],[],[],[]]

matriz[0].append("|1ª etapa")
matriz[0].append("|2ª etapa")
matriz[0].append("|3ª etapa|")
prim = float("inf")
segund = float("inf")
terceira = float("inf")

for i in range(1,6):
    for j in range(3):
        valor = int(input("Digite o valor:"))
        matriz[i].append(valor)
        if j == 0:
            if prim > matriz[i][j]:
                prim = matriz[i][j]
                comp1 = i
        elif j == 1:
            if segund > matriz[i][j]:
                segund = matriz[i][j]
                comp2 = i
        elif j == 2:
            if terceira > matriz[i][j]:
                terceira = matriz[i][j]
                comp3 = i
for i in range (6):
    for j in range(3):
        if i>0:
            print(f"{matriz[i][j]}s", end=" | ")
        else:
            print(f"{matriz[i][j]}", end="")
    print()

print("\nMenores Tempos")
print(f"1º Etapa: Competidor {comp1} com {prim}s")
print(f"2º Etapa: Competidor {comp2} com {segund}s")
print(f"3º Etapa: Competidor {comp3} com {terceira}s")