import os

def processar_frase():
    maior_palavra = ""
    
    while True:
        frase = input()
        if frase == "0":
            break

        palavras = frase.split()
        tamanhos = "-".join(str(len(palavra)) for palavra in palavras)
        print(tamanhos)

        for palavra in palavras:
            if len(palavra) >= len(maior_palavra):
                maior_palavra = palavra

    return maior_palavra

def main():
    os.system('cls')
    maior_palavra = processar_frase()
    print(f"\nThe biggest word: {maior_palavra}")

if __name__ == "__main__":
    main()