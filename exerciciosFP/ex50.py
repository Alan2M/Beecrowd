import os
os.system('cls')

def wordcount(frase,maiorpalavra):
    frase = input()
    palavras = frase.split()
    for i in palavras:
        if len(palavras[i]) > len(palavras[i-1]):
            maiorpalavra = len(palavras[i])
while True:
    frase = input()
    palavras = frase.split()
    for i in palavras:
        if len(palavras[i]) > len(palavras[i-1]):
            maiorpalavra = len(palavras[i])
    if frase == "0":
        break
print(f"The biggest word: {maiorpalavra}")