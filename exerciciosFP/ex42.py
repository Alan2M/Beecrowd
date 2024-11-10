import os
os.system('cls')

lista = ["cheia de manias", "me leava junto com você", "é tarde demais", "quando te encontrei", "deus me livre", "ciumes de voce", "cigana"]

def index(n1,n2):
    i = n1 + n2
    return lista[i]

botao1 = int(input("Digite o valor do primeiro botão: "))
botao2 = int(input("Digite o valor do segundo botão: "))

if botao1+botao2 > 6 or botao1 > 5 or botao2 > 5:
    print("Fora do intervalo")

else:
    print(index(botao1,botao2))