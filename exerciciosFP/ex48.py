import os
os.system('cls')

romanos = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}

n = -1
while n <= 0 or n >= 1000:
    n = int(input())

rom = []
for valor, simbolo in romanos.items():
    while n >= valor:
        rom.append(simbolo)
        n -= valor

print("".join(rom))
