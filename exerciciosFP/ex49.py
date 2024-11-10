def wordcount(n, a, b):
    count = n.split()
    a = 0
    b = ""
    for i in range(len(count)):
        count[i] = len(count[i])
        if count[i] > a:  # Use o valor diretamente de count[i]
            a = count[i]
            b = n.split()[i]  # Atribui a palavra correspondente a 'b'
    return count, b  # Retorna a lista de tamanhos e a maior palavra

a = 0
b = ""
while True:
    frase = input()
    if frase == "0":
        break
    tamanho, b = wordcount(frase, a, b)

print("-".join(map(str, tamanho)))
print(f"\nThe biggest word: {b}")