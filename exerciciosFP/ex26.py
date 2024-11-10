import os
os.system('cls')

quadrados = {}
n = int(input("Digite um numero inteiro:"))

for i in range(n+1):
    quadrados[i] = i*i
print(quadrados)