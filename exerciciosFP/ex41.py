import os
os.system('cls')

def sum(n1,n2):
    return (n1+n2)
def sub(n1,n2):
    return (n1-n2)
def mult(n1,n2):
    return (n1*n2)
def div(n1,n2):
    if n2 == 0:
        return print("Erro: Divisão por zero!")
    return (n1/n2)

while True:
    num1 = int(input("Digite o primeiro numero para realizar a operação: "))
    num2 = int(input("Digite o segundo numero para realizar a operação: "))
    operação = input("Qual operação deseja realizar? ").lower()
    if operação == "soma":
        print(sum(num1,num2))
    elif operação == "subtração":
        print(sub(num1,num2))
    elif operação == "multiplicação":
        print(mult(num1,num2))
    elif operação == "divisão":
        print(div(num1,num2))
    resp = input("Deseja continuar ou encerrar? ").lower()
    if resp == "encerrar":
        break
