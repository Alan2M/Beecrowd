import os
os.system('cls')

c = {
    'suco de laranja': 120, 
    'morango fresco': 85, 
    'mamao': 85, 
    'goiaba vermelha': 70, 
    'manga': 56, 
    'laranja': 50, 
    'brocolis': 34
} 

def vitcalc(n):
    vitamina = 0
    for _ in range(n):
        entrada = input().split()
        quantidade = int(entrada[0])
        fruta = ' '.join(entrada[1:])
        vitamina += c.get(fruta, 0) * quantidade
    return vitamina