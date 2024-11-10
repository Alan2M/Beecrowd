import os
os.system('cls')

intervalo1 = int(input("Digite o primeiro numero do intervalo: "))
intervalo2 = int(input("Digite o segundo numero do intervalo: "))
soma=0

while intervalo1 <= intervalo2:
    
    if intervalo1%2 == 0:
        soma += intervalo1
    intervalo1 += 1

print("A soma dos pares é:",soma)