import os
os.system('cls')

def maior_palavra_na_frase(frase, maiorpalavra_atual):
    palavras = frase.split()
    tamanhos = "-".join(str(len(palavra)) for palavra in palavras)
    print(tamanhos)

    for palavra in palavras:
        if len(palavra) >= len(maiorpalavra_atual): 
            maiorpalavra_atual = palavra

    return maiorpalavra_atual

def main():
    maiorpalavra = ""
    while True:
        frase = input().strip()
        if frase == "0":
            break
        maiorpalavra = maior_palavra_na_frase(frase, maiorpalavra)

    print(f"The biggest word: {maiorpalavra}")

main()