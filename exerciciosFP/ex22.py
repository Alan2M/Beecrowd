import os
os.system('cls')

inteiros = []
pares = []
impares = []
for i in range (10):
    inteiros.append(int(input("Digite um numero inteiro:")))
print(inteiros)
for inteiros in inteiros:
    if inteiros%2==0:
        pares.append(inteiros)
    if inteiros%2!=0:
        impares.append(inteiros)
print(impares)
print(pares)