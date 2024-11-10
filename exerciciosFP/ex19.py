import os
os.system('cls')
palavra = []
for i in range(5):
    palavra.append(input("Digite uma palavra:"))
palavra.sort()
for palavra in palavra:
    print(palavra)