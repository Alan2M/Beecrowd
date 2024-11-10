import os
os.system('cls')

def calc(inicial,atual):
    dif = inicial - atual
    percentual = dif/inicial * 100

    return percentual

inicial = float(input("Digite o peso inicial: "))
atual = float(input("Digite o peso atual: "))
    
print(calc(inicial,atual))