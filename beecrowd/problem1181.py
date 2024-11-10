import os
os.system('cls')
import string

matriz = [] * 12
n = 12
s = 0

L = input()
V = input()
for i in range(n):

    if V == "S":
        s = s + matriz[i]
    if V == "M":
        media = s/n
    for j in range(n):
        matriz[L].append(float(input()))
if V == "S":
    print(s)
if V == "M":
    print(media)