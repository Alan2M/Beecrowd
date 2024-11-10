import os
os.system('cls')

nomes = []
idades = []

mais_idoso = 0
n = 0

funcionarios_aptos = int(input("Digite a quantidade de funcionarios aptos a aposentadoria: "))
for i in range(funcionarios_aptos):
    nome = input("Digite o nome completo do funcionario: ")
    idade = int(input("Digite a idade do funcionario: "))
    while idade<60:
        print("Funcionario ainda não pode se aposentar ")
        nome = input("Digite o nome completo de outro funcionario: ")
        idade = int(input("Digite a idade do funcionario: "))
    if n < idade:
        n = idade
        mais_idoso = nome
    nomes.append(nome)
    idades.append(idade)

media = sum(idades)/funcionarios_aptos

print("\nFuncionários a se aposentar em 2025")
print("--------------------------------------\n")
for i in range(funcionarios_aptos):
    print(f"Nome: {nomes[i]}\t Idade: {idades[i]} anos")
print(f"\nFuncioário mais antigo: {mais_idoso}")
print(f"Media de idades das aposentadorias: {media} anos")