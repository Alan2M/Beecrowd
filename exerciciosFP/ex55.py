import os
os.system('cls')

dicionario = {}

while True:
    try:
        for nome in range(2):
            tsum = 0
            nome = input("Digite o nome do corredor: ")
            for j in range(3):
                tempo = int(input(f"Qual foi o tempo de {nome} na {j+1}ª volta: "))
                tsum += tempo
            dicionario[nome] = "Media de tempo:",tsum/3
        print(dicionario)
        break
    except ValueError:
        print("Digite um numero valido!")