import os 
os.system('cls')

matriz = []

n = int(input())
for i in range(3):
    matriz.append([])
    for j in range(3):
        n = n*2
        matriz[i].append(n)

for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]",end="")
    print()