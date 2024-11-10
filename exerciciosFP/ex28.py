import os
os.system('cls')

nomes = []

while True:
    print("1 CREATE")
    print("2 READ")
    print("3 UPDATE")
    print("4 DELETE")
    print("5 ENCERRAR")

    cod = int(input("DIGITE 1, 2, 3, 4 ou 5 para realizar a ação correspondente:\n"))

    if cod == 1:
        nome = str(input("Digite um nome para adicionar:\n"))
        nomes.append(nome)
    elif cod == 2:
        print(nomes)
    elif cod == 3:
        indice = int(input("Digite o indice que deseja atualizar:\n"))
        if 0 <= indice < len(nomes):
            nomes[indice] = str(input("Digite o nome que deseja adicionar:\n"))
    elif cod == 4:
        indice = int(input("Digite o indice que deseja deletar:\n"))
        if 0 <= indice < len(nomes):
            indice.pop(indice)
    elif cod == 5:
        print("Programa encerrado")
        break