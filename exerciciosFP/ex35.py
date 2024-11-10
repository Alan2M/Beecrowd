import os
os.system('cls')

nome = []
idade = []
p = 0
quantidade = int(input("Digite a quantidade de funcionarios aptos a aposentadoria: "))
for i in range(quantidade):
    n = input("Digite o nome completo do funcionario: ")
    id = int(input("Digite a sua idade: "))
    while id<60:
        print("Funcionario ainda não pode se aposentar, insira um funcionario com idade válida: ")
        n = input("Digite o nome completo do funcionario: ")
        id = int(input("Digite a sua idade: "))
    nome.append(n)
    idade.append(id)
    if id > p:
        antigo = nome[i] 
        p = id
print("Funcionarios a se aposentar em 2025")
print("************************************\n")
for i in range(quantidade):
    print(f"Nome: {nome[i]} \tIdade: {idade[i]} anos")

media = sum(idade)/quantidade
print(f"Funcionario mais antgio: {antigo}")
print(f"Media de idade das aposentadorias: {media} anos")