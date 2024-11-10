import os
os.system('cls')

quantidade = int(input("Digite quantas equações deseja calcular as raizes:"))

for i in range(quantidade):
    a = float(input("Digite o valor de A:"))
    if a != 0:
        b = float(input("Digite o valor de B:"))
        c = float(input("Digite o valor de C:"))
        delta =  (b**2 - 4*a*c)
        bhaskara1 = (-b + delta**(1/2))/2*a
        bhaskara2 = (-b - delta**(1/2))/2*a
        if delta<0:
            print("Não possui raizes reais")
        elif delta==0:
            print(bhaskara1)
        else:
            print("Primeira raiz:",bhaskara1,"\nSegunda raiz:",bhaskara2)
    else:
        print("A equação não é do segundo grau")
    