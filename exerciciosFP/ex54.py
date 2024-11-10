import os
os.system('cls')

while True:
    try:
        n = int(input("Digite um numero inteiro: "))
        print(f"A raiz quadrada de {n} é igual a: {n**(1/2)}")
        break
    except ValueError:
        print("Digite um numero valido!")