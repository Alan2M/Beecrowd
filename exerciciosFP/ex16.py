import os
os.system('cls')

n = int(input("Digite um numero para verificar se ele é perfeito: "))
ns = 0
for i in range(1,n):
    if n%i==0:
        ns += i
if ns==n:
    print("Ele é perfeito")
else:
    print("Não é perfeito")