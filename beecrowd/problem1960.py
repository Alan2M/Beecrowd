import os
os.system('cls')

rom = []
n = -1

# Garantir que o número esteja entre 1 e 999
while n <= 0 or n >= 1000:
    n = int(input("Digite um número entre 1 e 999: "))

# Construa o número romano usando ifs
if n >= 1000:
    rom.append('M')
    n -= 1000

if n >= 900:
    rom.append('CM')
    n -= 900

if n >= 500:
    rom.append('D')
    n -= 500

if n >= 400:
    rom.append('CD')
    n -= 400

if n >= 100:
    while n >= 100:
        rom.append('C')
        n -= 100

if n >= 90:
    rom.append('XC')
    n -= 90

if n >= 50:
    rom.append('L')
    n -= 50

if n >= 40:
    rom.append('XL')
    n -= 40

if n >= 10:
    while n >= 10:
        rom.append('X')
        n -= 10

if n >= 9:
    rom.append('IX')
    n -= 9

if n >= 5:
    rom.append('V')
    n -= 5

if n >= 4:
    rom.append('IV')
    n -= 4

if n >= 1:
    while n >= 1:
        rom.append('I')
        n -= 1

# Exibir o número romano como string
print("".join(rom))
