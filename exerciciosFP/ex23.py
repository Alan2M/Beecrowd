import os
os.system('cls')

lista = []
print("[1] CREATE")
print("[2] READ")
print("[3] UPDATE")
print("[4] DELETE")
print("[5] ENCERRAR")
codigo = int(input("Digite a ação que deseja realizar:"))

while True:
    if codigo == 1:
        lista.append(input("Adicione um nome a lista:"))

        codigo = int(input("Digite a ação que deseja realizar:"))
    elif codigo == 2:
        print("Lista de nomes")
        for indice, nome in enumerate(lista):
            print(f"{indice} - {nome}")

        codigo = int(input("Digite a ação que deseja realizar:"))
    elif codigo == 3:
        indice = int(input("Digite o indice que deseja atualizar:"))
        if 0<=indice<len(lista):
            novo_nome = input("Digite o nome que deseja atualizar:")
            lista[indice] = novo_nome
        else:
            print("Valor invalido")

        codigo = int(input("Digite a ação que deseja realizar:"))
    elif codigo == 4:
        indice = int(input("Digite o indice que deseja apagar:"))
        if 0<=indice<len(lista):
            lista.pop(indice)
        else:
            print("Valor invalido")

        codigo = int(input("Digite a ação que deseja realizar:"))
    elif codigo == 5:
        print("Programa encerrado.")
        break