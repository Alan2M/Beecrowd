import os
os.system('cls')


rom = []
n = -1
while n <= 0 or n >= 1000:
    n = int(input())

m = 1000
d = 500
c = 100
l = 50
x = 10
v = 5
I = 1

if n//d >= 1:
    rom.append('D')
    n = n-d
if n//c >= 1:
    for i in range(n//c):
        rom.append('C')
    n = n - c*(n//c)
if n//l >= 1:
    for i in range(n//l):
        rom.append('L')
    n = n - l*(n//l)
if n//x >= 1:
    for i in range(n//x):
        rom.append('X')
    n = n - x*(n//x)
if n//v >= 1:
    for i in range(n//v):
        rom.append('V')
    n = n - v*(n//v)
if n//I >= 1:
    for i in range(n//I):
            rom.append('I')
    n = n - I*(n//I)

print(rom)