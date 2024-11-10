import os
os.system('cls')

def  media_valores(valor1,valor2):
    media = (valor1+valor2)/2
    return media

def status(media):
    if media>=7:
        print("Aprovado")

nota1 = int(input())
nota2 = int(input())

media = media_valores(nota1,nota2)

print(media)

status(media)