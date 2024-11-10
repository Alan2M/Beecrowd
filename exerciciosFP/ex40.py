import os
os.system('cls')

def wordcount(n):
    
    count = n.split()
    return len(count)

frase = input("Digite a frase: ")
print(wordcount(frase))